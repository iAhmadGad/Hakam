import sys, subprocess, threading
from frontend import print_dots

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
LIGHT_WHITE="\033[97m"
LIGHT_GREEN="\033[38;5;48m"

result_dict = {
    "passed_count": 0,
    "wrong_count": 0,
    "error_count":0,
    "results": []
}

def compile(compile_command):
    compile_result = subprocess.run(compile_command, shell=True)
    if compile_result.returncode != 0:
        sys.exit(f"Compilation failed with code {compile_result.returncode}")

def execute(execute_command, tests, strict, verbose):
    for i in range(len(tests)):
        test = tests[i]
        input_data = test[0].encode().decode('unicode_escape')  # Interpret escape sequences
        try:
            result = subprocess.run(
            execute_command,
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
            )
            output = result.stdout.decode().strip()
            if result.returncode != 0:
                if verbose:
                    result_dict["results"].append(f"{LIGHT_WHITE}{i}: {RED}Execution failed with code {result.returncode}")
                    result_dict["results"][-1] += f"\n{RED}{result.stderr.decode()}{RESET}"
                    
                result_dict["error_count"] += 1                
                if strict:
                     sys.exit(result_dict["results"][-1])
                    
            elif output == test[1]:
                if verbose:
                    result_dict["results"].append(f"{LIGHT_WHITE}{i + 1}: {GREEN}Test Passed :){RESET}")
                result_dict["passed_count"] += 1
            else:
                if verbose:
                    result_dict["results"].append(f"{LIGHT_WHITE}{i + 1}: {RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")
                result_dict["wrong_count"] += 1
                if strict:
                    sys.exit(f"{LIGHT_WHITE}{i + 1}: {RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")

        except subprocess.CalledProcessError as e:
            sys.exit(f"{RED}Execution Command failed with error code {e.returncode}: {e.output.decode()}{RESET}")

    return result_dict
            
def test(test_dict, strict = False, verbose = False):
    stop_event = threading.Event()

    if "compile" in test_dict:
        print("Compiling...", end="")
        stop_event.clear()
        t1 = threading.Thread(target=print_dots, args=(stop_event,))
        t2 = threading.Thread(target=compile, args=(test_dict["compile"],))
        t1.start()
        t2.start()

        t2.join()
        stop_event.set()
        t1.join()
        print()

    if "execute" in test_dict:
        print("Testing...", end="")
        stop_event.clear()
        t1 = threading.Thread(target=print_dots, args=(stop_event,))
        t2 = threading.Thread(target=execute, args=(test_dict["execute"], test_dict["tests"], strict, verbose))
        t1.start()
        t2.start()

        t2.join()
        stop_event.set()
        t1.join()
        print()

    return result_dict
