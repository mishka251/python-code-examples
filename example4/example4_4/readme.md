# Пример 4.4 - создание и установка двух пакетов пространства имён

1. Создадим ППИ `functions` в папке `functions`, аналогично 4.3
2. Создадим ППИ `functions` с дополнительными функциями в папке `functons_extra`
3. Создадим и активируем `venv` в папке `project`

В папке `projectA/venv/Lib/site-packages` появится папка `functions`, содержащая модули как из `functions/functions`, так и из `functions_extra/functions`
