from test_methods.add import add # пример относительного импорта
from test_methods.sub import sub # пример абсолютного импорта
from test_methods.mul import mul
from test_methods.div import div


def get_method(operator):
    method = None
    if operator == '+':
        method = add
    elif operator == '-':
        method = sub
    elif operator == '*':
        method = mul
    elif operator == '/':
        method = div

    if method is None:
        raise ValueError('Метод не найден')
    return method
