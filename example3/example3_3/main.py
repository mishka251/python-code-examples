import functions  # Также не рабочий пример

a = float(input('Введите первое число: '))
operator_sign = input('Введите знак операции: ')
b = float(input('Введите второе число: '))

function = functions.get_function.get_function(operator_sign)  # здесь будет ошибка - модули не являются атрибутами пакета
result = function(a, b)
print(result)
