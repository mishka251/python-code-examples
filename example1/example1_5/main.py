import functions # импортируем весь модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function(operator_sign) # вызов функции аналогичен примеру 1
result = function(a, b)
print(result)

# этот код НЕ сломается
# вызов функции не смотря на __all__
print(functions.add(1, 2))
