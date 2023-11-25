"""
Для списка numbers подсчитать сумму элементов с помощью функции reduce.

numbers = [3, 4, 6, 9, 34, 12]
Создайте функцию sum_numbers(numbers), результатом выполнения которой будет сумма чисел всех элементов списка numbers.

"""
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def sum_numbers(numbers):
    sum = reduce((lambda x, y: x + y), numbers)
    return sum

print(sum_numbers(numbers))