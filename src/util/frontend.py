from time import sleep
from util.colors import RESET, BOLD, RED, YELLOW, LIGHT_WHITE, LIGHT_GREEN

def print_dots(stop_event):
    while not stop_event.is_set():
        print(".", end="", flush=True)
        sleep(0.5)

def get_tests(tests_number):
    tests = []
    for i in range(tests_number):
        print("Input:")
        _input = ""
        try:
            while True:
                _input += input() + "\n"
        except EOFError:
            pass
        print("Output:")
        output = ""
        try:
            while True:
                output += input() + "\n"
        except EOFError:
            pass
        tests.append([_input.strip(), output.strip()])
    return tests

def print_results(results):

    for result in results:
        print(result)

def print_final_result(passed_count, wrong_count, error_count):
    
     if not (error_count or wrong_count):
        print(f"{BOLD}{LIGHT_GREEN}Accepted{RESET}")
     else:
        if passed_count:
            print(f"{LIGHT_GREEN}Passed: {LIGHT_WHITE}{passed_count}{RESET}")
        if wrong_count:
            print(f"{RED}Wrong answers: {LIGHT_WHITE}{wrong_count}{RESET}")
        if error_count:
            print(f"{YELLOW}Errors: {LIGHT_WHITE}{error_count}{RESET}")
