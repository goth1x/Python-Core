"""
Поработаем немного со спецификацией в форматировании строк. 
Напишите функцию formatted_numbers, которая возвращает список 
отформатированных строк, чтобы при выводе следующего кода:

for el in formatted_numbers():
    print(el)
Получалась следующая таблица:

| decimal  |   hex    |  binary  |
|0         |    0     |         0|
|1         |    1     |         1|
|2         |    2     |        10|
|3         |    3     |        11|
|4         |    4     |       100|
|5         |    5     |       101|
|6         |    6     |       110|
|7         |    7     |       111|
|8         |    8     |      1000|
|9         |    9     |      1001|
|10        |    a     |      1010|
|11        |    b     |      1011|
|12        |    c     |      1100|
|13        |    d     |      1101|
|14        |    e     |      1110|
|15        |    f     |      1111|

все столбцы имеют ширину в 10 символов
у заголовков таблицы выравнивание по центру
первый столбец десятичных чисел — выравнивание по левому краю
второй столбец шестнадцатеричных чисел — выравнивание по центру
третий столбец двоичных чисел — выравнивание по правому краю
вертикальный символ | не входит в ширину столбца
Как вы уже поняли, функция formatted_numbers выводит таблицу чисел 
от 0 до 15 в десятичном, шестнадцатеричном и двоичном формате.

"""

def formatted_numbers():
    spisok = ['|{:^10}|{:^10}|{:^10}|'.format('decimal','hex','binary')]
    for i in range(16):
        spisok.append(f'|{i:<10d}|{i:^10x}|{i:>10b}|')
    return spisok

for el in formatted_numbers():
    print(el)