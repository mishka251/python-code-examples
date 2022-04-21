from methods import get_method, plus

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign)
result = method(a, b)
print(result)
