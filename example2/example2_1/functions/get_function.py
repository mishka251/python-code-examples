from functions.add import add # пример относительного импорта
from functions.sub import sub # пример абсолютного импорта
from functions.mul import mul
from functions.div import div


def get_function(operator):
    function = None
    if operator == '+':
        function = add
    elif operator == '-':
        function = sub
    elif operator == '*':
        function = mul
    elif operator == '/':
        function = div

    if function is None:
        raise ValueError('Метод не найден')
    return function
