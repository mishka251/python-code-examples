from methods import *  # импортируем всё из файла methods/__init__

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method.get_method(operator_sign)  # Будет ошибка, т.к. __init__ пустой
result = method(a, b)
print(result)
