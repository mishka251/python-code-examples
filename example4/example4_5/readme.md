# Пример 4.5 - попытка установки двух пакетов с одинаковым содержимым

1. Создадим пакет `functions` в папке `functions`, аналогично 4.3
2. Создадим пакет `functions` с дополнительными функциями в папке `functons_extra`
3. Создадим и активируем `venv` в папке `project`
4. Установим командой `pip install .` оба пакета. В результате будет один пакет `venv\Lib\site-packags\functions`, содержащий модули из обоих пакетов. `__init__.py` будет взят из последнего по порядку запуска установки пакета