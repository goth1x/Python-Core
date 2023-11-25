"""
Создайте класс NumberString, наследуйте его от класса UserString, 
определите для него метод number_count(self), 
который будет считать количество цифр в строке.
"""
    
from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count
    
string = NumberString('определите дл3я него ме6тод n4umber_count(self), кот4орый будет счит3ать количество цифр в строке.')
print(string.number_count())