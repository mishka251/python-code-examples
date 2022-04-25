from test_methods.get_method import get_method
from test_methods.pow import pow


def get_method_extra(operator):
    if operator == '**':
        return pow
    return get_method(operator)
