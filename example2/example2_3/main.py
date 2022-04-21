import methods  # Также не рабочий пример, т.к. из namespace package не получается импортировать модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = methods.get_method.get_method(operator_sign)  # здесь будет ошибка
result = method(a, b)
print(result)
