# Пример 5.2 - два пакета с одним пространством имён на PyPi

1. Сделаем в папке `methods` пакет пространств имён `test_methods`, опубликуем его на тестовом PyPi под названием `mishka251-test-methods-namespace`
2. Создадим второй проект в папке `methods_extra`, содержащий пакет пространства имён `test_methods` опубликуем его на тестовом PyPi под названием `mishka251-test-methods-namespace-extra`
3. В папке проекта `project` создадим виртуальное окружение `python -m venv venv` и активируем его `venv/Scripts/activate`
4. Установим в `project` как зависимости обе библиотеки `pip install -i https://test.pypi.org/simple/ mishka251-test-methods-namespace`, `pip install -i https://test.pypi.org/simple/ mishka251-test-methods-namespace-extra`
5. Т.к. в обоих пакетах есть пакет пространств имён `test_methods`, в результате мы получаем один ППИ
