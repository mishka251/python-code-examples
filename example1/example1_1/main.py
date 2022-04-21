import methods  # импортируем модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = methods.get_method(operator_sign)  # в таком случае модуль используется как пространство имён и функцию вызываем из него
result = method(a, b)
print(result)
