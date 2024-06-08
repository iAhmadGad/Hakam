import time

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
LIGHT_WHITE="\033[97m"
LIGHT_GREEN="\033[38;5;48m"

def print_dots(stop_event):
    while not stop_event.is_set():
        print(".", end="", flush=True)
        time.sleep(0.5)

def print_results(results):

    for result in results:
        print(f"{result}\n", end="")

def print_final_result(passed_count, wrong_count, error_count):
    
     if not (error_count or wrong_count):
        print(f"{BOLD}{LIGHT_GREEN}Accepted{RESET}")
     else:
        if passed_count:
            print(f"{LIGHT_GREEN}Passed: {LIGHT_WHITE}{passed_count}{RESET}")
        if wrong_count:
            print(f"{RED}Wrong answers: {LIGHT_WHITE}{wrong_count}{RESET}")
        if error_count:
            print(f"{YELLOW}Runtime wrrors: {LIGHT_WHITE}{error_count}{RESET}")
