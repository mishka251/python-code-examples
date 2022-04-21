a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def get_method(operator):
    method = None
    if operator == '+':
        method = add
    elif operator == '-':
        method = sub

    if method is None:
        raise ValueError('Метод не найден')
    return method


method = get_method(operator_sign)
result = method(a, b)
print(result)
