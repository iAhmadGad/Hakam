import sys
from test import test

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
LIGHT_WHITE="\033[97m"

USAGE="Usage: hakam [command] <candidate> <option>\n\ncommands:\n\thelp\n\tnew : new testlistfile with name 'hakam.json'\n\tnew <name> : new testlistfile with name <name>.json\n\ttest : test file with name 'hakam.json'\n\ttest <name> : test file with name <name>.json\n\noptions:\n\t--strict : strict mode exits when code gives wrong answers or throws runtims error".expandtabs(4)
HAKAMFILE='{\n\t"compile": ""\n\t,"execute": ""\n\t,"tests":\n\t[\n\t\t["", ""]\n\t\t,["", ""]\n\t]\n}'.expandtabs(4)

def main():
    if sys.argv[1] == "test":
        if len(sys.argv) == 2:
            test("hakam.json")
        elif len(sys.argv) == 3:
            if sys.argv[2] == "--strict":
                test("hakam.json", strict = True)
            else:
                test(sys.argv[2])
        else:
            test(sys.argv[2], strict = True)
    elif sys.argv[1] == "new":
        if len(sys.argv) == 2:
            f = open("hakam.json", "w")
            f.write(HAKAMFILE)
            f.close()
        else:
            f = open(f"{sys.argv[2]}.json", "w")
            f.write(HAKAMFILE)
            f.close()
    elif sys.argv[1] == "help":
        sys.exit(USAGE)
    else:
        sys.exit(USAGE)
        
if __name__ == "__main__":
    main()
