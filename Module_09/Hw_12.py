"""
Вернемся к нашей первой задаче с четвертого модуля и перепишем ее с помощью функции reduce.

payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам в конце месяца 
— список payment. Задолженности могут быть отрицательными — у нас переплата, или положительными, 
если необходимо оплатить по счетам. С помощью reduce просуммируйте положительные значения и сумму 
платежа в конце месяца верните из функции amount_payment.
"""

from functools import reduce

payment = [1, -3, 4, -12, -8, 5]

def amount_payment(payment):
    sum = reduce((lambda x, y: x + y if x > 0 and y > 0 else x), payment)
    return sum

print(amount_payment(payment))