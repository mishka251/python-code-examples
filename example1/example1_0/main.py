from methods import get_method # импорт функции из модуля

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

method = get_method(operator_sign) # вызываем импортированную функцию также, как если бы она была в этом файла
result = method(a, b)
print(result)
