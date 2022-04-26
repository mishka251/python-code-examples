import test_variables
print('В main', test_variables.a, test_variables.b)
test_variables.a = 100 # Пример ПЛОХОГО кода - изменение глобальной переменной другого модуля
test_variables.b = 200
print('В main', test_variables.a, test_variables.b)

from test_functions import print_variables
print_variables()
