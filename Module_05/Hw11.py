"""
Для закрепления материала напишите функцию find_all_words, которая ищет 
совпадение слова в тексте. Функция возвращает список всех нахождений слова 
в параметре word в тексте в любом виде написания, т.е. например, возможные 
варианты написания слова "Python" как pYthoN, pythOn, PYTHOn и т.д. главное, 
чтобы сохранялся порядок слов, регистр не имеет значение.

Подсказка: функции модуля re принимают еще последний параметр flags и 
мы можем определить нечувствительность к регистру, присвоив ему 
значение re.IGNORECASE
"""

import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC"\
       "programming language, and first released it in 1991 as Python 0.9.0."

word = "pYthOn"

def find_all_words(text, word):
    found = re.findall(word, text, flags=re.IGNORECASE)
    return found

print(find_all_words(text, word))