from test_mthods.add import add # пример относительного импорта
from test_mthods.sub import sub # пример абсолютного импорта
from test_mthods.mul import mul
from test_mthods.div import div


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
