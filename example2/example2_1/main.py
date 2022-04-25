from functions import get_function  # импортируем модуль get_function из пакета functions

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = get_function.get_function(operator_sign)  # вызываем метод get_function из модуля get_function
result = function(a, b)
print(result)

# Пример ПЛОХОГО кода - вызов метода add из модуля get_function, хотя add там только импортируется, а определена в другом
print(get_function.add(1, 2))
