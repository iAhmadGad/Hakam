import argparse
from test import test
from file import new, set, add, remove
from util.frontend import print_results, print_final_result
from util.colors import RESET, LIGHT_WHITE
    
def main():
    parser = argparse.ArgumentParser(description="Hakam (Problem solving judge)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # New command
    parser_new = subparsers.add_parser("new", help="Create a new test file")
    parser_new.add_argument("--filename", "-f", default="hakamfile.json", help="Name of the test file to create")
    parser_new.add_argument("--compile", "-c", metavar="command", default="", help="Compile command")
    parser_new.add_argument("--execute", "-e", metavar="command", default="", help="Execute command")
    parser_new.add_argument("--tests", "-t", metavar="number",default=0, help="Number of tests")

    # Set command
    parser_set = subparsers.add_parser("set", help="Set values in a test file")
    parser_set.add_argument("--filename", "-f", default="hakamfile.json", help="Name of the test file to add values")
    parser_set.add_argument("--compile", "-c", metavar="command", default="", help="Set compile command")
    parser_set.add_argument("--execute", "-e", metavar="command", default="", help="Set execute command")
    parser_set.add_argument("--tests", "-t", metavar="number", help="Number of tests to set, overrides any existing tests")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add values to a test file")
    parser_add.add_argument("--filename", "-f", default="hakamfile.json", help="Name of the test file to add values")
    parser_add.add_argument("--compile", "-c", metavar="command", default="", help="Add compile command")
    parser_add.add_argument("--tests", "-t", metavar="number", help="Number of tests to add")

    # Remove command
    parser_rm = subparsers.add_parser("rm", help="Remove values from a test file")
    parser_rm.add_argument("--filename", "-f", default="hakamfile.json", help="Name of the test file to add values")
    parser_rm.add_argument("--compile", "-c", action="store_true", help="Remove compile command")
    parser_rm.add_argument("--test", "-t", metavar="index", help="Index of tests to remove")

    # Test command
    parser_test = subparsers.add_parser("test", help="Run tests on a test file")
    parser_test.add_argument("--filename", "-f", default="hakamfile.json", help="Name of the test file to test")
    parser_test.add_argument("--strict", "-s", action="store_true", help="Exit if code answered wrong or if runtime error is thrown")
    parser_test.add_argument("--verbose", "-v", action="store_true", help="Print tests & results")
    
    args = parser.parse_args()
    
    if args.command == "new":
        new(args.filename, args.compile, args.execute, args.tests)
        print(f"{LIGHT_WHITE}Created new test file: {args.filename}{RESET}")

    elif args.command == "set":
        set(args.filename, args.compile, args.execute, args.tests)
        print(f"{LIGHT_WHITE}Set values in test file: {args.filename}{RESET}")

    elif args.command == "add":
        add(args.filename, args.compile, args.tests)
        print(f"{LIGHT_WHITE}Added values to test file: {args.filename}{RESET}")

    elif args.command == "rm":
        remove(args.filename, args.compile, args.test)
        print(f"{LIGHT_WHITE}Removed values from test file: {args.filename}{RESET}")

    elif args.command == "test":
        result_dict = test(args.filename. args.strict, args.verbose)
        print_results(result_dict["results"])
        print_final_result(result_dict["passed_count"], result_dict["wrong_count"], result_dict["error_count"])         

if __name__ == "__main__":
    main()
    
