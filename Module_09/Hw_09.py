"""
Вначале четвертого модуля мы решали задачу выплат по коммунальным платежам. 
Они представляли собой список payment с положительными и отрицательными значениями.
Создайте функцию positive_values и с помощью функции filter отфильтруйте список 
payment по положительным значениям, и верните его из функции.

payment = [100, -3, 400, 35, -100]

"""
payment = [100, -3, 400, 35, -100]

def positive_values(list_payment):
    values = filter(lambda x: x > 0, list_payment)
    return list(values)


print(positive_values(payment))


