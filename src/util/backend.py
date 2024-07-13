import sys
from multiline import load, dumps

def get_test_dict(filename):
    try:
        with open(filename, "r") as f:
            return load(f, multiline=True)
    except FileNotFoundError:
        sys.exit(f"Error: {filename} not found")
    

def set_test_file(filename, test_dict):
      with open(filename, "w") as f:
            f.write(dumps(test_dict, indent=4))
