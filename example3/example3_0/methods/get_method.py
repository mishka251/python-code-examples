from .add import add # пример относительного импорта
from methods.sub import sub # пример абсолютного импорта
from .mul import mul
from .div import div


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
