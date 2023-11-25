"""
Подсписком (sublist) называют список, являющийся составной частью большего списка. 
Подсписок может содержать один элемент, множество элементов, а также быть пустым.

Например, [1], [2], [3] и [4] являются подсписками списка [1, 2, 3, 4]. Список [2, 3] 
также входит в состав [1, 2, 3, 4], но при этом список [2, 4] не является подсписком [1, 2, 3, 4], 
поскольку в исходном списке числа 2 и 4 не соседствуют.

Пустой список является подсписком для любого списка.

Напишите функцию all_sub_lists, возвращающую список, содержащий все возможные подсписки заданного.

Например, если функции передан аргумент список [1, 2, 3], то функция должна вернуть следующий 
список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функция all_sub_lists должна возвращать как минимум один список с пустым подсписком [[]].

"""


def all_sub_lists(data):
    sub_lists = [[]]
    if len(data) == 0:
        return sub_lists
    elif len(data) == 1:
        sub_lists.append(data)
        return sub_lists

    for element in data:
        sub_lists.append([element])
    if len(data) > 1:
        k = len(data) - 2
    for n in range(k):
        for i in range(len(data)):
            sub_lists.append(data[i-1:i+n+1]) if len(data[i-1:i+n+1]
                                                     ) > 0 and data[i-1:i+n+1] not in sub_lists else None
    sub_lists.append(data)
    return sub_lists


print(all_sub_lists([1,3,4,5]))



def all_sub_lists2(data):
    B = [[]]

    for i in range(len(data)+1):
        for j in range(i+1, len(data) + 1):
            sub = data[i:j]
            B.append(sub)
    return sorted(B, key=len)
    
print(all_sub_lists2([1,3,4,5]))