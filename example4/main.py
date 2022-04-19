# from methods import get_method, plus
from methods.main import get_method, plus #warn! не делайте так

a = float(input('Первое число'))
operator_character = input('Оператор')
b = float(input('Второе число'))

method = get_method(operator_character)
result = method(a, b)
print(result)
