from test_methods.get_method_extra import get_method_extra
from test_methods.pow import pow

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method_extra(operator_sign)  # здесь будет method.get_method - уже функция, т.к. она импортирована в __init__
result = method(a, b)
print(result)

print(pow(3, 4))
