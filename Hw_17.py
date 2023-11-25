"""
Вернемся к предыдущей задаче и выполним обратную задачу. 
Напишите рекурсивную функцию encode для кодирования списка или строки. 
В качестве аргумента функция принимает список 
( например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]) 
или строку (например "XXXZZXXYYYZZ"). Функция должна вернуть закодированный 
список элементов (пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

"""


def encode(data):
    if isinstance(data, str):
        data = list(data)
    encoded = []
    count = 1
    if len(data) == 0:
        return encoded
    else:
        char = data[0]
    encoded.append(data.pop(0))
    while len(data) > 0:
        if data[0] == char:
            count += 1
            data.pop(0)
        else:
            break
    encoded.append(count)
    encoded.extend(encode(data))
    return encoded


data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Y", "Z", "Z"]
data = "XXXZZXXYYYZZ"

print(encode(data))
