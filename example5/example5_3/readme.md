# Пример 5.3 - два пакета с одним пространством имён, установка из соседней папки

1. Сделаем в папке `functions` пакет пространств имён `test_functions`
2. Создадим второй проект в папке `functions_extra`, содержащий пакет пространства имён `test_functions`
3. В папке проекта `project` создадим виртуальное окружение `python -m venv venv` и активируем его `venv/Scripts/activate`
4. Установим в `project` как зависимости обе библиотеки ссылками `pip install -e file:../functions#egg=mishka251-test-functions-namespace`, `pip install -e file:../functions_extra#egg=mishka251-test-functions-namespace-extra`
5. Проверяем работоспособность - всё работает
