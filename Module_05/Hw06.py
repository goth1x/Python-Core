"""
Рассмотрим задачу на проверку спама в email письме или фильтрацию запрещенных слов в сообщении.

Пусть функция is_spam_words принимает строку (параметр text), проверяет её на содержание 
запрещённых слов из списка (параметр spam_words), и возвращает результат проверки: True, 
если есть хоть одно слово из списка, и False, если в тексте стоп-слов не обнаружено.

Слова в параметре text могут быть в произвольном регистре, а значит функция is_spam_words, 
при поиске запрещённых слов, регистронезависима и весь текст должна сводить к нижнему регистру. 
Для упрощения, будем считать, что в строке присутствует только одно запрещенное слово.

Предусмотреть третий параметр функции space_around, который по умолчанию равен False. 
Он отвечает за то, что функция будет искать отдельное слово или нет. Слово считается стоящим 
отдельно, если слева от слова находится символ пробела или оно расположено в начале текста, 
а справа от слова находится пробел или символ точки.

Например, в тексте мы ищем слово "лох". То в слове "Молох" вызов и результат будет следующим:

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
т.е. во втором случае слово не отдельное и является частью другого.

В этом примере, функция вернет True в обоих случаях.

print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
"""

# def is_spam_words(text, spam_words, space_around=False):
#     for word in spam_words:
#         if word.lower() in text.lower():
#             index = text.lower().find(word.lower())
#             if not space_around:
#                 return True
#             else:
#                 if (text[index - 1] == ' ' or text[index - 1] == '') and (text[index + len(word)] == ' ' or text[index + len(word)] == '.'):
#                     return True
#     return False




def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if space_around:
            return word.lower() in text.lower().removesuffix('.').split(' ')
        else:
            return word.lower() in text.lower()
    return False



print(is_spam_words("Молох", ["лох"]))
print(is_spam_words("Молох", ["лох"], True))
print(is_spam_words("Ты лох.", ["лох"]))
print(is_spam_words("Ты лох.", ["лох"], True))