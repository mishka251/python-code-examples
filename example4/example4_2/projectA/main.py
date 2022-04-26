from functions.get_function import get_function

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function(operator_sign)
result = function(a, b)
print(result)
