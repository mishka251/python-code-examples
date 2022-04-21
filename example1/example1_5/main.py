import methods # импортируем весь модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = methods.get_method(operator_sign) # вызов функции аналогичен примеру 1
result = method(a, b)
print(result)

# этот код НЕ сломается
# вызов функции не смотря на __all__
print(methods.add(1, 2))
