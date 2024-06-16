import sys, subprocess, threading
from util.backend import get_test_dict
from util.frontend import print_dots, print_results, print_final_result
from util.colors import RESET, RED, GREEN, LIGHT_WHITE

def compile(compile_command):
    compile_result = subprocess.run(compile_command, shell=True)
    if compile_result.returncode != 0:
        sys.exit(f"Compilation failed with code {compile_result.returncode}")

def execute(execute_command, tests, strict, verbose, result_dict):
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
                result_dict["error_count"] += 1                
                result = f"""{LIGHT_WHITE}{i}: {RED}Execution failed with code {result.returncode}
{RED}{result.stderr.decode()}{RESET}"""
                if verbose:
                    result_dict["results"].append(result)                    
                if strict:
                     sys.exit()
                    
            elif output == test[1].strip():
                result_dict["passed_count"] += 1
                result = f"{LIGHT_WHITE}{i + 1}: {GREEN}Test Passed :){RESET}"
                if verbose:
                    result_dict["results"].append(result)
            else:
                result_dict["wrong_count"] += 1
                result = f"""{LIGHT_WHITE}{i + 1}: {RED}Wrong Answer :^){RESET}
{LIGHT_WHITE}input:{RESET}
{test[0]}
{RED}output:{RESET}
{output}
{LIGHT_WHITE}expected:{RESET}
{test[1]}"""
                if verbose:
                    result_dict["results"].append(result)
                if strict:
                    sys.exit()

        except subprocess.CalledProcessError as e:
            sys.exit(f"{RED}Execution Command failed with error code {e.returncode}:\n{e.output.decode()}{RESET}")


def test(filename, strict, verbose):
    test_dict = get_test_dict(filename)

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

    result_dict = {
        "passed_count": 0,
        "wrong_count": 0,
        "error_count":0,
        "results": []
        }
        
    if "execute" in test_dict:
        print("Testing...", end="")
        stop_event.clear()
        t1 = threading.Thread(target=print_dots, args=(stop_event,))
        t2 = threading.Thread(target=execute, args=(test_dict["execute"], test_dict["tests"], strict, verbose, result_dict))
        t1.start()
        t2.start()

        t2.join()
        stop_event.set()
        t1.join()
        
        print()

    print_results(result_dict["results"])
    if not strict: print_final_result(result_dict["passed_count"], result_dict["wrong_count"], result_dict["error_count"])         
    