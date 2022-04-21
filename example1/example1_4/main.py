from methods import get_method, add # импортируем две функции не смотря на __all__

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign) # вызов функции аналогичен примеру 1
result = method(a, b)
print(result)

# этот код НЕ сломается
print(add(1, 2))
