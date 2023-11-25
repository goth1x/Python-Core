"""
Мы имеем следующую структуру файла:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Каждая запись состоит из трех частей и начинается с новой строки. 
Например, для первой записи начало 60b90c1c13067a15887e1ae1 — это 
первичный ключ базы данных MongoDB. Он всегда содержит 12 байт или 
ровно 24 символа. Дальше мы видим кличку кота Tayson и его возраст 3. 
Все части записи разделены символом запятая ,

Разработайте функцию get_cats_info(path), которая будет возвращать 
список словарей с данными кошек в виде:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
Параметры функции:

path - путь к файлу
Требования:

прочтите содержимое файла, используя режим "r".
мы используем менеджер контекста with
верните из функции список кошек из файла в требуемом формате

"""
path = 'D:\\Projects\cats.txt'


def get_cats_info(path):
    with open(path, 'r') as file:
        cat_list = []
        while True:
            cat_dict = {}
            line = file.readline().removesuffix('\n')
            if not line:
                break
            line_list = line.split(',')
            cat_dict = {'id': line_list[0],
                        'name': line_list[1], 'age': line_list[2]}
            cat_list.append(cat_dict)
        file.close()
        return cat_list


print(get_cats_info(path))
