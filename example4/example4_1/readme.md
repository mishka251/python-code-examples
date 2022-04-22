# Пример простейшей python-библиотеки 

В предыдущем примере мы импортировали сразу get_methods, что неудобно, ведь ожидается использование `test-methods`. Для этого в папке с библиотекой `methods` создадим `test-methods`

Получившаяся структура

    methods/
        test_methods/   <- эта папка будет установлена как библиотека
            __init__.py
            add.py
            get_method.py
            ...
        setup.py <- а что устанавливать указано здесь