# Пример простейшей python-библиотеки 

До этого мы использовали глобальный python-интерпретатор, однако часто удобнее разделять зависимости для разных проектов.
Python позволяет для каждого из проектов создать своё виртуальное окружение - venv, собственный интерпретатор с библиотеками. Для этого используется virtualenv
Для создания в папке проекта(projectA и projectB) используем команду `python -m venv venv` (`python -m venv` - запуск создания виртуального окружения, `venv` - аргумент с названием папки, в которой будет создано вирутальное окружение. venv общепринятое название, но может быть другим)
Папка venv обычно лежит в gitignor-е
Далее необходимо активировать виртуальное окружение(`venv\Scripts\activate` в папке проекта для Windows)
Далее переходим в папку `methods` и повторно используем `pip install .`
После этого пакет `test_methods` появится в `projectA/venv/Lib/site-packages`
Отключить виртуальное окружение можно командой `deactivate`