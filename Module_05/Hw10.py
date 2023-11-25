"""

Напишите функцию find_word, которая принимает два параметра: первый text и второй word. 
Функция выполняет поиск указанного слова word в тексте text с помощью функции search и возвращает словарь.

При вызове функции:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC 
    programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат должен быть следующего вида при совпадении:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor 
    to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
где

result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию
Если совпадений не обнаружено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor 
    to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor 
    to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}

"""

import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC"\
       "programming language, and first released it in 1991 as Python 0.9.0."

word = "released"


def find_word(text, word):
    find_dict = {}
    found = re.search(word, text)
    if found:
        find_dict['result'] = True
        find_dict['first_index'] = found.start()
        find_dict['last_index'] = found.end()
        find_dict['search_string'] = found.group()
        find_dict['string'] = found.string
    else:
        find_dict['result'] = False
        find_dict['first_index'] = None
        find_dict['last_index'] = None
        find_dict['search_string'] = word
        find_dict['string'] = text
    return find_dict


print(find_word(text, word))
