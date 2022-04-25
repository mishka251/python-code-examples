from functions import get_function  # импорт функции из модуля

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function(operator_sign)  # вызываем импортированную функцию также, как если бы она была в этом файла
result = function(a, b)
print(result)
