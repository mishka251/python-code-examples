from methods.get_method import get_method  # импортируем из модуля methods.get_method функцию get_method

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign)
result = method(a, b)
print(result)
