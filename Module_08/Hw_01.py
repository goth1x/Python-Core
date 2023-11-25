"""
Разработайте функцию get_days_from_today(date), 
которая будет возвращать количество дней от текущей даты, 
где параметр date — это строка формата '2020-10-09' (год-месяц-день).

Подсказки:

Параметр date разбить на год, месяц и день можно, используя метод строк split.
datetime принимает аргументы типа int, используйте преобразование типов.
игнорируйте часы, минуты и секунды для вашей даты, важны полные дни.
количество дней вы можете получить вычитанием из текущей даты, заданной в date (без времени).
Например: Если текущая дата — 5 мая 2021, то вызов get_days_from_today("2021-10-09") вернет нам -157.

"""

from datetime import datetime


def get_days_from_today(date):
    data = date.split('-')
    d1 = datetime(year=int(data[0]), month=int(data[1]), day=int(data[2]))
    delta = datetime.now() - d1
    return delta.days



date = '2023-11-09' 
print(get_days_from_today(date))