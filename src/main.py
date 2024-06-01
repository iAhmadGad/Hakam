import sys, os, subprocess, multiline

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
LIGHT_WHITE="\033[97m"

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <some_argument> <path_to_test_file>")
        return
    
    f = open(sys.argv[2], "r")
    testList = multiline.load(f)
    f.close()

    print("Compiling...")
    if "compile" in testList:
        compile_command = testList["compile"]
        compile_result = subprocess.run(compile_command, shell=True)
        if compile_result.returncode != 0:
            print(f"Compilation failed with code {compile_result.returncode}")
            return

    print("Executing...")
    if "execute" in testList:
        for test in testList["tests"]:
            input_data = test[0].encode().decode('unicode_escape')  # Interpret escape sequences
            expected_output = test[1]
            try:
                result = subprocess.run(
                    testList['execute'],
                    input=input_data.encode(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
                output = result.stdout.decode().strip()
                if result.returncode != 0:
                    print(f"Execution failed with code {result.returncode}")
                    print(result.stderr.decode())
                elif output == expected_output:
                    print(f"{GREEN}Test Passed :){RESET}")
                else:
                    print(f"{RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")
            except subprocess.CalledProcessError as e:
                print(f"Command failed with error code {e.returncode}: {e.output.decode()}")

if __name__ == "__main__":
    main()
