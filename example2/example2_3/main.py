import methods  # импортируем всех модулей из пакета methods

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = methods.get_method.get_method(operator_sign)  # вызываем метод get_method из модуля get_method
result = method(a, b)
print(result)
