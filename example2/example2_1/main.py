from methods import get_method  # импортируем модуль get_method из пакета methods

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method.get_method(operator_sign)  # вызываем метод get_method из модуля get_method
result = method(a, b)
print(result)

# Пример ПЛОХОГО кода - вызов метода add из модуля get_method,
print(get_method.add(1, 2))
