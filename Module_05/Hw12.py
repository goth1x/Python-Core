"""
В шестой задаче мы писали функцию is_spam_words, которая определяла, 
есть или нет стоп-слова в тексте сообщения. Давайте пойдем дальше и 
применим функцию sub модуля re для замены указанных в списке стоп-слов 
на некоторый шаблон. Например, все "плохие" слова будем заменять 
звездочками. Напишите функцию replace_spam_words, которая принимает 
строку (параметр text), проверяет её на содержание запрещённых слов 
из списка (параметр spam_words), и возвращает результат строку, 
но вместо запрещенных слов, подставлен шаблон из *, причем длина 
шаблона равна длине запрещенного слова. Определить нечувствительность 
к регистру стоп-слов.

"""

import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, len(word)*'*', text, flags=re.IGNORECASE)
    return text

print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))

        
    