import sys
from test import test

RESET="\033[0m"
BOLD="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
LIGHT_WHITE="\033[97m"

USAGE="Usage: python main.py test <path_to_test_list_file>"

def main():
    if not len(sys.argv) == 3:
        sys.exit(USAGE)
    if sys.argv[1] != "test":
    	sys.exit(USAGE)
    
    test(sys.argv[2])
        
if __name__ == "__main__":
    main()
