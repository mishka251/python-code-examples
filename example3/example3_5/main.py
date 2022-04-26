import functions

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function(operator_sign)  # за счёт импорта в __init__ пример рабочий
result = function(a, b)
print(result)
