def cost_delivery(quantity, *_, discount = 0):
    '''Функция возвращает общую сумму доставки.

    Первый параметр указывает количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.'''
        
    return ((quantity - 1) * 2 + 5) * (1 - discount)
print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))
print(cost_delivery.__doc__)