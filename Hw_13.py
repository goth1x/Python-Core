"""
Есть файл со списком сотрудников компании. В каждой строке файла записана 
информация только про одного сотрудника. Формат записи, в учебных целях, 
упрощенный в виде имени сотрудника, символа пробела и его должности, т.е. кем он работает.

John courier
Pipe cook
Создайте функцию get_employees_by_profession(path, profession). Функция должна 
в файле (параметр path) найти всех сотрудников указанной профессии (параметр profession)

Требования:

откройте файл при помощи with для чтения.
получите строки из файла при помощи метода readlines()
с помощью метода find найдите все строки в файле, где есть указанная profession, 
и поместите записи в список.
объедините все эти строки в списке в одну строку при помощи метода join (помните 
про перевод строк '\n' и лишние пробелы, которые надо убрать).
уберите значение 'profession' (замените на пустую строку "" при помощи метода replace).
верните итоговую строку из файла

"""
from pathlib import Path

path = Path(r'C:\Users\goth2\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\1C\Космические Рейнджеры\new_text.txt')


def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        name = []
        all_lines = file.readlines()
        for line in all_lines:
            if line.find(profession) != -1:
                name.append(line.removesuffix(
                    '\n').replace(profession, '').strip())
        string = ' '.join(name)
    return string


print(get_employees_by_profession(path, 'cook'))
