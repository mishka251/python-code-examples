from get_method import get_method

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign)  # здесь будет method.get_method - уже функция, т.к. она импортирована в __init__
result = method(a, b)
print(result)
