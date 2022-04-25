from functions import *  # импортируем всех модулей из пакета functions

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function.get_function(operator_sign)  # Будет ошибка, т.к. у namespace package нет информации о всех модулях
result = function(a, b)
print(result)
