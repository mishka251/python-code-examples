from functions import *  # импортируем всё из файла functions/__init__

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function.get_function(operator_sign)  # Работает, т.к. модуль get_function импортирован в __init__.py
result = function(a, b)
print(result)
