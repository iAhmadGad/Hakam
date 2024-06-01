import sys, subprocess, multiline

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
LIGHT_WHITE="\033[97m"
LIGHT_GREEN="\033[38;5;48m"

def test(testListFile):
        f = open(testListFile, "r")
        testList = multiline.load(f)
        f.close()

        print("Compiling...")
        if "compile" in testList:
                compileCommand = testList["compile"]
                compileResult = subprocess.run(compileCommand, shell=True)
                if compileResult.returncode != 0:
                        sys.exit(f"Compilation failed with code {compileResult.returncode}")

            
        ls = []
        passedCount = 0
        wrongCount = 0
        errorCount = 0
            
        print("Executing...")
        if "execute" in testList:
                for i in range(len(testList["tests"])):
                        test = testList["tests"][i]
                        inputData = test[0].encode().decode('unicode_escape')  # Interpret escape sequences
                        try:
                                result = subprocess.run(
                                        testList['execute'],
                                        input=inputData.encode(),
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=True
                )
                                output = result.stdout.decode().strip()
                                if result.returncode != 0:
                                        ls.append(f"{LIGHT_WHITE}{i}: {RED}Execution failed with code {result.returncode}")
                                        ls[-1] += f"\n{RED}result.stderr.decode(){RESET}"
                                        errorCount += 1
                                elif output == test[1]:
                                        ls.append(f"{LIGHT_WHITE}{i}: {GREEN}Test Passed :){RESET}")
                                        passedCount += 1
                                else:
                                        ls.append(f"{LIGHT_WHITE}{i}: {RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")
                                        wrongCount += 1

                        except subprocess.CalledProcessError as e:
                                ls.append(f"{RED}Command failed with error code {e.returncode}: {e.output.decode()}{RESET}")
                
        for e in ls:
      	        print(f"{e}\n", end="")

        if passedCount == len((testList["tests"])):
                print(f"{BOLD}{LIGHT_GREEN}Accepted{RESET}")
        else:
                if passedCount:
                        print(f"{LIGHT_GREEN}Passed: {LIGHT_WHITE}{passedCount}{RESET}")
                if wrongCount:
                        print(f"{RED}Wrong answers: {LIGHT_WHITE}{wrongCount}{RESET}")
                if errorCount:
                        print(f"{YELLOW}Runtime wrrors: {LIGHT_WHITE}{errorCount}{RESET}")
