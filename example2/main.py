from methods import get_method, plus

a = float(input('Первое число'))
operator_character = input('Оператор')
b = float(input('Второе число'))

method = get_method(operator_character)
result = method(a, b)
print(result)
