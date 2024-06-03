import sys
from test import test

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
LIGHT_WHITE="\033[97m"

USAGE="Usage: hakam <command> [candidate] [option]\n\ncommands:\n\thelp\n\tnew : new test file with name 'testfile.json'\n\tnew [testfile] : new test file with name [testfile]\n\ttest : test file with name 'testfile.json'\n\ttest [testfile] : test file with name [testfile]\n\noptions:\n\t--strict : makes Hakam exits if your code answered wrong or if runtime error is thrown".expandtabs(4)
TESTFILE='{\n\t"compile": ""\n\t,"execute": ""\n\t,"tests":\n\t[\n\t\t["", ""]\n\t\t,["", ""]\n\t]\n}'.expandtabs(4)

def main():
    if sys.argv[1] == "test":
        if len(sys.argv) == 2:
            test("testfile.json")
        elif len(sys.argv) == 3:
            if sys.argv[2] == "--strict":
                test("testfile.json", strict = True)
            else:
                test(sys.argv[2])
        else:
            test(sys.argv[2], strict = True)
    elif sys.argv[1] == "new":
        if len(sys.argv) == 2:
            f = open("testfile.json", "w")
            f.write(TESTFILE)
            f.close()
        else:
            f = open({sys.argv[2]}, "w")
            f.write(TESTFILE)
            f.close()
    elif sys.argv[1] == "help":
        sys.exit(USAGE)
    else:
        sys.exit(USAGE)
        
if __name__ == "__main__":
    main()
