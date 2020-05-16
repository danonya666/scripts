This script automates the process of building star ephemeris objects.
It parses the data.xlsm file and puts the result to output.xlsm
Sample file is provided

How to run:
`pip install -r requirements.txt`
`python script.py`

Как запускать для чайников:
0. Положить файл data.xlsm в папку со скриптом
1. Если не установлен python - скачать + установить с https://www.python.org/downloads/windows/
2. Открыть командую строку (Пуск, выполнить, cmd)
3. С помощью команды cd перейти в папку со скриптом и файликами
    a) cd .. - перейти в родительскую папку
    б) cd <имя_папки> - перейти в папку с <именем>
    в) на Windows - dir, на нормальных системах ls - посмотреть что в текущей папке
3,5. `pip install -r requirements.txt`
4. `python script.py`
5. Должно работать, если не работает, посмотрите пункты 1-4