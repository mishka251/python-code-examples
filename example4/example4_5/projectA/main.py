from functions.get_function_extra import get_function_extra
from functions.pow import pow

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function_extra(operator_sign)
result = function(a, b)
print(result)

print(pow(3, 4))
