import functions  # Также не рабочий пример, т.к. из namespace package не получается импортировать модуль
from functions.add import add

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function(operator_sign)  # здесь будет function.get_function - уже функция, т.к. она импортирована в __init__
result = function(a, b)
print(result)

print(add(1, 2))
