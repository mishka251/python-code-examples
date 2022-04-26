import functions  # Также не рабочий пример, т.к. из namespace package не получается импортировать модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function.get_function(operator_sign)  # Здесь будет ошибка. PyCharm этого не показывает
result = function(a, b)
print(result)
