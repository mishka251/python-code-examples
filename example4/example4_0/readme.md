# Пример простейшей python-библиотеки 

Для того, чтобы другие проекты могли использовать functions, необходимо добавить в него файл, отвечающий за его установку. `setup.py`

Файл `setup.py` содержит вызов функции `setuptools.setup`, в которую передаются аргументы с информацией о библиотеке.
Для примера назовём её `test-functions`.

Для локальной установки библиотеки необходимо использовать `pip install .` в папке, содержащей `setup.py`.

После установки всё содержимое библиотеки будет помещено в папку с python-библиотеками. На этом компьютере `C:\Python39\Lib\site-packages`
Т.к. в папке `functions` лежат файлы, а не папки то их необходимо явно указать в `setup.py`, как `py_modules`, автоматически могут обнаруживаться только пакеты.
Также импортируются потом именно эти файлы, без указания библиотеки `functions`, что не очевидно.
