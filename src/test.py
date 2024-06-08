import sys, subprocess, multiline, threading
from frontend import print_dots

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
LIGHT_WHITE="\033[97m"
LIGHT_GREEN="\033[38;5;48m"

results = []
passed_count = 0
wrong_count = 0
error_count = 0

def compile(compile_command):
    compile_result = subprocess.run(compile_command, shell=True)
    if compile_result.returncode != 0:
        sys.exit(f"Compilation failed with code {compile_result.returncode}")

def execute(execute_command, test_dict, strict):
    global passed_count, wrong_count, error_count
    for i in range(len(test_dict["tests"])):
        test = test_dict["tests"][i]
        input_data = test[0].encode().decode('unicode_escape')  # Interpret escape sequences
        try:
            result = subprocess.run(
            test_dict['execute'],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
            )
            output = result.stdout.decode().strip()
            if result.returncode != 0:
                results.append(f"{LIGHT_WHITE}{i}: {RED}Execution failed with code {result.returncode}")
                results[-1] += f"\n{RED}result.stderr.decode(){RESET}"
                error_count += 1
                if strict:
                    sys.exit(ls[-1])
            elif output == test[1]:
                results.append(f"{LIGHT_WHITE}{i}: {GREEN}Test Passed :){RESET}")
                passed_count += 1
            else:
                results.append(f"{LIGHT_WHITE}{i}: {RED}Wrong Answer :^)\n{RESET}expected {LIGHT_WHITE}{test[1]} {RESET}for input {LIGHT_WHITE}{test[0]} {RESET}not {RED}{output}")
                wrong_count += 1
                if strict:
                    sys.exit(results[-1])

        except subprocess.CalledProcessError as e:
            results.append(f"{RED}Command failed with error code {e.returncode}: {e.output.decode()}{RESET}")            

def print_results():
    
    for result in results:
        print(f"{result}\n", end="")

def print_final_result(test_dict):
    
     if passed_count == len((test_dict["tests"])):
        print(f"{BOLD}{LIGHT_GREEN}Accepted{RESET}")
     else:
        if passed_count:
            print(f"{LIGHT_GREEN}Passed: {LIGHT_WHITE}{passed_count}{RESET}")
        if wrong_count:
            print(f"{RED}Wrong answers: {LIGHT_WHITE}{wrong_count}{RESET}")
        if error_count:
            print(f"{YELLOW}Runtime wrrors: {LIGHT_WHITE}{error_count}{RESET}")

            
def test(test_file, strict = False, verbose = False):
    f = open(test_file, "r")
    test_dict = multiline.load(f)
    f.close()

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
        print("Executing...", end="")
        stop_event.clear()
        t1 = threading.Thread(target=print_dots, args=(stop_event,))
        t2 = threading.Thread(target=execute, args=(test_dict["execute"], test_dict, strict))
        t1.start()
        t2.start()

        t2.join()
        stop_event.set()
        t1.join()
        print()

    if verbose:
        print_results()

    print_final_result(test_dict)
