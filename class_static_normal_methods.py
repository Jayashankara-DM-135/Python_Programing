# Class method: Which takes class as parameter
#               It can be called using Class name and object as well
#               ususally used Class name.
#               Defined under @classmethod

                # It can be used as alternative constuctor

# Static method: Which does not take object or Class as a parameter.
#                It's called using Class name.
#                Defined under @staticmethod

# Normal method: Which takes object as parameter.
#                Its called using object.

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
