# Пример ограничения возможности импорта содержимого модуля


Примечания:

- В отличие от `example1_2` В модуль `methods.py` добавлено ограничение `import *` - константа `__all__` со списком имён, которые будут импортированы при использовании такого импорта
- В `main.py` можно вызывать только `get_method`
