"""
Создайте функцию decimal_average(number_list, signs_count), 
которая будет вычислять среднее арифметическое типа Decimal
 с количеством значащих цифр signs_count.

number_list — список чисел

Внимание
Не забывайте приводить все числа в списке к типу `decimal`

Пример:

вызов функции decimal_average([3, 5, 77, 23, 0.57], 6) вернет 21.714
вызов функции decimal_average([31, 55, 177, 2300, 1.57], 9) вернет 512.91400

"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    numbers = [Decimal(i) for i in number_list]
    result = Decimal(sum(numbers)) / Decimal(len(numbers))
    return result


print(decimal_average([3, 5, 77, 23, 0.57], 6))
# 21.714
