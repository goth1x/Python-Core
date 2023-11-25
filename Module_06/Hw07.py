"""
Разработайте функцию sanitize_file(source, output), 
переписывающую в текстовый файл output содержимое текстового файла source, очищенное от цифр.

Требования:

прочтите содержимое файла source, используя менеджер контекста with и режим "r".
запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
запись нового содержимого файла output должна быть единоразовая и использовать метод write

"""
import re
source = 'D:\\Projects\Rawtext.txt'
output = 'D:\\Projects\Cleartext.txt'


def sanitize_file(source, output):
    with open(source, 'r') as src:
        sanitize = ''.join(re.findall(r'\D', src.read()))
    with open(output, 'w') as out:
        out.write(sanitize)


sanitize_file(source, output)
