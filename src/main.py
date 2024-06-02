import sys
from test import test

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
LIGHT_WHITE="\033[97m"

USAGE="Usage: python main.py test <path_to_test_list_file>"
HAKAMFILE='{\n\t"compile": ""\n\t,"execute": ""\n\t,"tests":\n\t[\n\t\t["", ""]\n\t\t,["", ""]\n\t]\n}'.expandtabs(4)

def main():
    if sys.argv[1] == "test":
        if len(sys.argv) == 2:
            test("hakam.json")
        else:
            test(sys.argv[2])
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
