import multiline

def get_test_dict(filename):
    with open(filename, "r") as f:
            return multiline.load(f, multiline=True)
    

def set_test_file(filename, test_dict):
      with open(filename, "w") as f:
            f.write(multiline.dumps(test_dict, indent=4))