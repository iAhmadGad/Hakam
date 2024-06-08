import argparse
from test import test

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

def create_test_file(filename):
    with open(filename, "w") as f:
        f.write(TESTFILE)
    print(f"{LIGHT_WHITE}Created new test file: {filename}{RESET}")

def run_tests(filename, strict, verbose):
    test(filename, strict=strict, verbose=verbose)
    
def main():
    parser = argparse.ArgumentParser(description="Hakam (Problem solving judge)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # New command
    parser_new = subparsers.add_parser("new", help="Create a new test file")
    parser_new.add_argument("--file", "-f", nargs="?", default="testfile.json", help="Name of the test file to create")

    # Test command
    parser_test = subparsers.add_parser("test", help="Run tests on a test file")
    parser_test.add_argument("--file", "-f", nargs="?", default="testfile.json", help="Name of the test file to test")
    parser_test.add_argument("--strict", "-s", action="store_true", help="Run tests in strict mode, which makes Hakam exit if your code didn't pass a test or a runtime error is thrown")
    parser_test.add_argument("--verbose", "-v", action="store_true", help="Print all the tests")

    args = parser.parse_args()

    if args.command == "new":
        create_test_file(args.file)
    elif args.command == "test":
        run_tests(args.file, args.strict, args.verbose)

if __name__ == "__main__":
    main()
