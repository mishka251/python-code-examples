from methods import *  # импортируем всех модулей из пакета methods

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method.get_method(operator_sign)  # Будет ошибка, т.к. у namespace package нет информации о всех модулях
result = method(a, b)
print(result)
