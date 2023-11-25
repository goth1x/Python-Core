"""
Напишите функцию для определения количества дней в конкретном месяце. 
Ваша функция должна принимать два параметра: month — номер месяца в 
виде целого числа в диапазоне от 1 до 12 и year — год, состоящий из 
четырех цифр. Убедитесь, что функция корректно обрабатывает февраль 
високосного года.

"""

from datetime import date


def get_days_in_month(month, year):
    day = 31
    while True:
        try:
            d1 = date(year=year, month=month, day=day)
            return day
        except ValueError:
            day -= 1
        
    
month = 2
year = 2001

print(get_days_in_month(month, year))