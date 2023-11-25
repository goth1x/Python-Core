"""
Все вы, возможно, сталкивались с ребусами "Найди слово". Они существуют как текстовые варианты, 
так и программы для мобильных приложений. Напомним кратко суть ребуса. В большом квадрате
 с набором бук необходимо найти слово по горизонтали и, иногда, по вертикали.

game
Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False) для 
нахождения искомого слова в строке ребуса.

Параметры функции:

riddle - строка с зашифрованным словом.
word_length - длина зашифрованного слова.
start_letter - буква, с которой начинается слово (подразумевается, что до начала слова буква не встречается в строке).
reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом. Для значения 
True слово зашифровано в обратном порядке, к примеру, в строке mi1rewopret зашифровано слово power.
Функция должна возвращать первое найденное искомое слово. Если слово не найдено, вернуть пустую строку.



"""


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    word = ''
    reverse = -1 if reverse else 1 
    if start_letter not in riddle:
        return word
    start_letter = riddle.find(start_letter)
    if word_length > len(riddle[start_letter::reverse]):
        return word
    else:
        
        return riddle[start_letter: start_letter + word_length * reverse: reverse]


print(solve_riddle('aaatttrrr', 5, 'p', True) )
