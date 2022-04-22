from test_methods.get_method import get_method
from test_methods.add import add

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign)  # здесь будет method.get_method - уже функция, т.к. она импортирована в __init__
result = method(a, b)
print(result)

print(add(1, 2))
