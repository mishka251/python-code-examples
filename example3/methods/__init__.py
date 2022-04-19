from .plus import plus
from .minus import minus
from .multiple import multiple


def get_method(operator):
    method = None
    if operator == '+':
        method = plus
    elif operator == '-':
        method = minus
    elif operator == '*':
        method = multiple

    if method is None:
        raise Exception('Метод не найден')
    return method
