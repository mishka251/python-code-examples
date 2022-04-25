a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def get_function(operator):
    function = None
    if operator == '+':
        function = add
    elif operator == '-':
        function = sub

    if function is None:
        raise ValueError('Метод не найден')
    return function


calculate_function = get_function(operator_sign)
result = calculate_function(a, b)
print(result)
