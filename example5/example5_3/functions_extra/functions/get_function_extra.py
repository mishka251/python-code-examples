from functions.get_function import get_function
from functions.pow import pow


def get_function_extra(operator):
    if operator == '**':
        return pow
    return get_function(operator)
