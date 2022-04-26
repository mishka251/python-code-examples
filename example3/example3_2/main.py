from functions import *  # импортируем всё из файла functions/__init__, но не все модули пакета functions

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function.get_function(operator_sign)  # Будет ошибка, т.к. __init__ пустой
result = function(a, b)
print(result)
