import 123functions # ОШИБКА название модуля начинается с цифр
import test-functions # ОШИБКА модуль содержит "-"
import test.functions # ОШИБКА модуль содержит ".". Python пытается найти модуль`functions` в библиотеке `test`, а не локальный файл `test.functions`


a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function(operator_sign) # вызов функции аналогичен примеру 1
result = function(a, b)
print(result)

# этот код НЕ сломается
# вызов функции не смотря на __all__
print(functions.add(1, 2))
