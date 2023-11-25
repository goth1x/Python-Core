"""
У нас есть именованный кортеж для хранения котов в переменной Cat. 
На первом месте у нас кличка котика nickname, потом его возраст age и имя владельца кота owner.

Разработайте функцию convert_list(cats), которая будет работать в двух режимах.

Если функция convert_list принимает в параметре cats список именованных кортежей

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
[Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]
То функция вернет следующий список словарей:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


И в то же время, если функция convert_list принимает в параметре cats список словарей, 
то результатом будет обратная операция и функция вернет список именованных кортежей.

Для определения типа параметра cats используйте функцию isinstance.

"""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cats_list = []
    if isinstance(cats[0], dict):
        for el in cats:
            el = list(el.values())
            cats_list.append(Cat(el[0],el[1],el[2]))
    else:
        for el in cats:
            cats_list.append({"nickname": el[0], "age": el[1], "owner": el[2]})
    return cats_list

cats = [{"nickname": "Mick", "age": 5, "owner": "Sara"},{"nickname": "Barsik", "age": 7, "owner": "Olga"},{"nickname": "Simon", "age": 3, "owner": "Yura"},]

print(convert_list(cats))
