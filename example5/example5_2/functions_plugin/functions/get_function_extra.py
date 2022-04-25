from test_functions.get_function import get_function
from test_functions.pow import pow


def get_function_extra(operator):
    if operator == '**':
        return pow
    return get_function(operator)
