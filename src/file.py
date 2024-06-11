from util.backend import get_test_dict, set_test_file
from util.frontend import get_tests

def new(filename, compile_command, execute_command, tests_number):
    test_dict = {}
    if compile_command:
        test_dict.update({"compile": compile_command})
    test_dict.update({
            "execute": execute_command,
            "tests": get_tests(int(tests_number))
            })
    
    set_test_file(filename, test_dict)


def set(filename, compile_command, execute_command, tests_number):
    test_dict = get_test_dict(filename)
    if compile_command:
        test_dict["compile"] = compile_command
    if execute_command:
        test_dict["execute"] = execute_command
    if tests_number:
        test_dict["tests"] = get_tests(int(tests_number))

    set_test_file(filename, test_dict)


def add(filename, compile_command, tests_number):
    test_dict = {}
    given_test_dict = get_test_dict(filename)
    if compile_command:
        test_dict.update({"compile": compile_command})
    test_dict.update({"execute": given_test_dict["execute"]})
    test_dict.update({"tests": given_test_dict["tests"]})
    if tests_number:
        test_dict["tests"].extend(get_tests(int(tests_number)))

    set_test_file(filename, test_dict)


def remove(filename, compile_command, test_index):
    test_dict = get_test_dict(filename)
    if compile_command:
        del test_dict["compile"]
    if test_index:
        del test_dict["tests"][int(test_index)]

    set_test_file(filename, test_dict)