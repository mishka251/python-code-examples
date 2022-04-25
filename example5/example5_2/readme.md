# Пример 5.2 - два пакета с одним пространством имён на PyPi

1. Сделаем в папке `functions` пакет пространств имён `test_functions`, опубликуем его на тестовом PyPi под названием `mishka251-test-functions-namespace`
2. Создадим второй проект в папке `functions_extra`, содержащий пакет пространства имён `test_functions` опубликуем его на тестовом PyPi под названием `mishka251-test-functions-namespace-extra`
3. В папке проекта `project` создадим виртуальное окружение `python -m venv venv` и активируем его `venv/Scripts/activate`
4. Установим в `project` как зависимости обе библиотеки `pip install -i https://test.pypi.org/simple/ mishka251-test-functions-namespace`, `pip install -i https://test.pypi.org/simple/ mishka251-test-functions-namespace-extra`
5. Т.к. в обоих пакетах есть пакет пространств имён `test_functions`, в результате мы получаем один ППИ
