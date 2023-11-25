"""
Реализуйте функцию file_operations(path, additional_info, start_pos, count_chars), 
которая добавляет дополнительную информацию в файл по пути path из параметра additional_info,
и после этого возвращает строку с позиции start_pos длиной count_chars.

Требования:

функция должна открывать файл с помощью with по пути path в режиме добавления информации
записывать в конец файла строку additional_info
после записи функция должна открыть тот же файл для чтения
прочитать и вернуть строку с позиции start_pos длиной count_chars с помощью функции seek.
Важно: для прохождения задачи необходимо использовать менеджер контекста with, методы seek, write и read.
"""
from pathlib import Path

path = Path(r'C:\Users\goth2\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\1C\Космические Рейнджеры\new_text.txt')
additional_info = 'Hello Max'


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as file:
        file.seek(start_pos)
        return file.read(count_chars)


print(file_operations(path, additional_info, 5, 5))
