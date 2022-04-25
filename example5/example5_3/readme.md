# Пример 5.3 - два пакета с одним пространством имён, установка из соседней папки

1. Сделаем в папке `methods` пакет пространств имён `test_methods`
2. Создадим второй проект в папке `methods_extra`, содержащий пакет пространства имён `test_methods`
3. В папке проекта `project` создадим виртуальное окружение `python -m venv venv` и активируем его `venv/Scripts/activate`
4. Установим в `project` как зависимости обе библиотеки ссылками `pip install -e file:../methods#egg=mishka251-test-methods-namespace`, `pip install -e file:../methods_extra#egg=mishka251-test-methods-namespace-extra`
5. Проверяем работоспособность - всё работает
