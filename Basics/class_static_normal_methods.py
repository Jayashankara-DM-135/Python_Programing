"""
Class method:
Methods which are defined using "@classmethod" keyword.
Class methids takes 'class' as parameter. It can be called using class name or object.
ususally class name used to call these methods.

Note: It can be used as a alternative constuctor.

================
Static method:
Methods which are defined using "@staticmethod" keyword.
Static method does not take any object or class as a parameter.
It's called using class name only.

================
 Normal method:
 Methods which are not defined using "@staticmethod or @classmethod"
 These methods takes object as parameter.
 Its called using object only.

"""
import datetime

class Empolyee:
    hike = 1.01

    def __init__(self, first, second, pay):
        self.first = first;
        self.second = second
        self.pay = pay

    def getFullName(self):
        return '{} {}'.format(self.first, self.second)

    @classmethod
    def raise_salary(cls, ammount):
        cls.hike = ammount

    @classmethod
    def from_string(cls, empstr):
        first, second, pay = empstr.split('-')
        return cls(first, second, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False;
        return True;


empstr1 = "Jayashankara-DM-100"
empstr2 = "ABD-RCB-1000000"


emp1 = Empolyee.from_string(empstr1)
emp2 = Empolyee.from_string(empstr2)


print(emp1.first)
print(emp2.second)

print(emp1.getFullName())
print(emp2.getFullName())

my_date = datetime.date(2016, 7, 6)
print(Empolyee.isWorkday(my_date))
