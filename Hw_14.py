"""
Напишите функцию to_indexed(source_file, output_file), которая будет считывать содержимое файла, 
добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.

Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела, 
после чего должен идти текст строки из исходного файла. Нумерация строк идет от 0.

"""
from pathlib import Path

path_r = Path(r'C:\Users\goth2\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\1C\Космические Рейнджеры\text.txt')
path_w = Path(r'C:\Users\goth2\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\1C\Космические Рейнджеры\new_text.txt')


def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file:
        lines = file.readlines()
    with open(output_file, 'w') as file:
        for i, line in enumerate(lines):
            file.write(f'{i}: {line}')


print(to_indexed(path_r, path_w))