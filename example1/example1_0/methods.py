def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def get_method(operator):
    method = None
    if operator == '+':
        method = add
    elif operator == '-':
        method = sub
    elif operator == '*':
        method = mul

    if method is None:
        raise ValueError('Метод не найден')
    return method
