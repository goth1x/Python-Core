"""
Есть две строки в разных кодировках - "utf-8" и "utf-16". 
Нам необходимо понять, равны ли строки между собой.

Реализуйте функцию is_equal_string(utf8_string, utf16_string), 
которая возвращает True, если строки равны между собой, и False — если нет.

"""

def is_equal_string(utf8_string, utf16_string):
    utf8 = utf8_string.decode()
    utf16 = utf16_string.decode('utf-16')
    return utf8 == utf16