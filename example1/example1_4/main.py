from functions import get_function, add # импортируем две функции не смотря на __all__

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function(operator_sign) # вызов функции аналогичен примеру 1
result = function(a, b)
print(result)

# этот код работает
print(add(1, 2))
