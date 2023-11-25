class Bankomat:
    def __init__(self, name, surname, balance=0):
        self.name = name
        self.surname = surname
        self.balance = balance
        
    def withdrow(self, value):
       if self.balance >= value and value > 0:
           self.balance -= value
       else:
           print("You don't have enough money")
    
    def add_money(self, value):
        self.balance += value
        
    def check_balance(self):
        print(f'You have: {self.balance} USD')
        
        
account1 = Bankomat("Jack", "Bower", 2500)
account2 = Bankomat("Emy", "Wong", 1500)

# account1.check_balance()
# account2.check_balance()
# account1.withdrow(1250)
# account1.add_money(100)
# account1.check_balance()


"""
Class Student System

Student -> Name, Surname, Grade, Birthday

Grade (from 0 to 100) -> (from 0 to 100), 'A', 'B', 'C'...

Class Student System -> (Students), find students where grade is equal to avarage
"""


class StudentSystem:
    def student_list(self, data_list):
        self.data_list = data_list
    def grade(self, mark):
        sys_grade = {1: 'F', 2: 'FX', 3: 'E',
                     3.5: 'D', 4: 'C', 4.5: 'B', 5: 'A'}
        final_mark = sys_grade.get(mark)
        return final_mark
    def avg_mark(self):
        sum = 0
        for students in self.data_list:
            sum += students.grade
        return sum / len(self.data_list)
    def find_student(self):
        avg_grade = self.avg_mark()
        for students in self.data_list:
            if avg_grade == students.grade:
                print(students.name)
class Students:
    def __init__(self, name, surname, grade, birthday):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.birthday = birthday
st_list = [Students('John', 'Doe', 3.5, '17.12.2013'),
           Students('Dick', 'Back', 4.5, '15.10.2011'),
           Students('Kel', 'Win', 4, '22.07.2012')]
c = StudentSystem()
c.student_list(st_list)

# print(c.grade(4))
# print(c.avg_mark())
# c.find_student()

class Detail:
    def __init__(self, name) -> None:
        self.name = name
    def __get__(self, instance, owner):
        return self.name
    def __set__(self, instance, name):
        self.name = name
    def __str__(self) -> str:
        return f"{self.name}"
class Motor(Detail):
    def __init__(self, name):
        super().__init__(name)
class Wheels(Detail):
    def __init__(self, name):
        super().__init__(name)
class Auto:
    details = []
    def add_detail(self, detail):
        self.details.append(detail)
motor1_5 = Motor("motor 1.5")
koleso = Wheels("wheels 17")
tavria = Auto()
tavria.add_detail(motor1_5)
tavria.add_detail(koleso)
print(tavria.details)