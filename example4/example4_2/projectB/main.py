from test_functions.get_function import get_function
from test_functions.add import add

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function(operator_sign)  # здесь будет function.get_function - уже функция, т.к. она импортирована в __init__
result = function(a, b)
print(result)

print(add(1, 2))
