import sys, subprocess, multiline, threading
from frontend import printDots

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
LIGHT_WHITE="\033[97m"
LIGHT_GREEN="\033[38;5;48m"

results = []
passedCount = 0
wrongCount = 0
errorCount = 0

def compile(compileCommand):
    compileResult = subprocess.run(compileCommand, shell=True)
    if compileResult.returncode != 0:
        sys.exit(f"Compilation failed with code {compileResult.returncode}")

def execute(executeCommand, testList, strict):
    global passedCount, wrongCount, errorCount
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
                results.append(f"{LIGHT_WHITE}{i}: {RED}Execution failed with code {result.returncode}")
                results[-1] += f"\n{RED}result.stderr.decode(){RESET}"
                errorCount += 1
                if strict:
                    sys.exit(ls[-1])
            elif output == test[1]:
                results.append(f"{LIGHT_WHITE}{i}: {GREEN}Test Passed :){RESET}")
                passedCount += 1
            else:
                results.append(f"{LIGHT_WHITE}{i}: {RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")
                wrongCount += 1
                if strict:
                    sys.exit(ls[-1])

        except subprocess.CalledProcessError as e:
            results.append(f"{RED}Command failed with error code {e.returncode}: {e.output.decode()}{RESET}")


def printResults(testList):
    for result in results:
        print(f"{result}\n", end="")

    if passedCount == len((testList["tests"])):
        print(f"{BOLD}{LIGHT_GREEN}Accepted{RESET}")
    else:
        if passedCount:
            print(f"{LIGHT_GREEN}Passed: {LIGHT_WHITE}{passedCount}{RESET}")
        if wrongCount:
            print(f"{RED}Wrong answers: {LIGHT_WHITE}{wrongCount}{RESET}")
        if errorCount:
            print(f"{YELLOW}Runtime wrrors: {LIGHT_WHITE}{errorCount}{RESET}")

def test(testFile, strict = False):
    f = open(testFile, "r")
    testList = multiline.load(f)
    f.close()

    stopEvent = threading.Event()

    if "compile" in testList:
        print("Compiling...", end="")
        stopEvent.clear()
        t1 = threading.Thread(target=printDots, args=(stopEvent,))
        t2 = threading.Thread(target=compile, args=(testList["compile"],))
        t1.start()
        t2.start()

        t2.join()
        stopEvent.set()
        t1.join()
        print()

    if "execute" in testList:
        print("Executing...", end="")
        stopEvent.clear()
        t1 = threading.Thread(target=printDots, args=(stopEvent,))
        t2 = threading.Thread(target=execute, args=(testList["execute"], testList, strict))
        t1.start()
        t2.start()

        t2.join()
        stopEvent.set()
        t1.join()
        print()

    printResults(testList)
