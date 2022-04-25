import functions  # импортируем модуль

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function(operator_sign)  # в таком случае модуль используется как пространство имён и функцию вызываем из него
result = function(a, b)
print(result)
