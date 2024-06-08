import argparse, multiline
from test import test
import frontend

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
LIGHT_WHITE = "\033[97m"

TESTFILE = """{
    "compile": "",
    "execute": "",
    "tests": [
        ["", ""],
        ["", ""]
    ]
}
"""
    
def main():
    parser = argparse.ArgumentParser(description="Hakam (Problem solving judge)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # New command
    parser_new = subparsers.add_parser("new", help="Create a new test file")
    parser_new.add_argument("testfile", nargs="?", default="testfile.json", help="Name of the test file to create")

    # Test command
    parser_test = subparsers.add_parser("test", help="Run tests on a test file")
    parser_test.add_argument("testfile", nargs="?", default="testfile.json", help="Name of the test file to test")
    parser_test.add_argument("--strict", "-s", action="store_true", help="exit if code answered wrong or if runtime error is thrown")
    parser_test.add_argument("--verbose", "-v", action="store_true", help="print tests & results")

    args = parser.parse_args()

    if args.command == "new":
        with open(args.testfile, "w") as f:
            f.write(TESTFILE)
        print(f"{LIGHT_WHITE}Created new test file: {args.testfile}{RESET}")

    elif args.command == "test":
        result_dict = {}
        with open(args.testfile, "r") as f:
            test_dict = multiline.load(f)
        result_dict = test(test_dict, strict=args.strict, verbose=args.verbose)
        frontend.print_results(result_dict["results"])
        frontend.print_final_result(result_dict["passed_count"], result_dict["wrong_count"], result_dict["error_count"])

if __name__ == "__main__":
    main()
    
