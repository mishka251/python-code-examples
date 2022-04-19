a = float(input('Первое число'))
operator_character = input('Оператор')
b = float(input('Второе число'))


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiple(a, b):
    return a * b


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


method = get_method(operator_character)
result = method(a, b)
print(result)
