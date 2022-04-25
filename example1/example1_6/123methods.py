def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def get_function(operator):
    function = None
    if operator == '+':
        function = add
    elif operator == '-':
        function = sub
    elif operator == '*':
        function = mul

    if function is None:
        raise ValueError('Метод не найден')
    return function


__all__ = ['get_function']  # появилось ограничения import *
