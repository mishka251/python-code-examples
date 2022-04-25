from functions import *  # импортируем ВСЕ функции, переменные и классы модуля.

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function(operator_sign)  # вызов функции аналогичен примеру 1
result = function(a, b)
print(result)

# пример того, что импортируется только функции, указанные в __all__
# этот код сломается
print(add(1, 2))
