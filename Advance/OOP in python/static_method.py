# static method will not take class name or object as parmeter. But it's called using class name or object name.
# usualy called using class name.

# Cretaed using @staticmethod decorator

# method should be static in case if we are not acessing instance or class anywhere in the method.


import datetime

class Employee:
    no_of_employee = 0
    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
        Employee.no_of_employee += 1


    def getFullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def set_raise_ammount(cls, ammount):
        cls.raise_ammount = ammount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @staticmethod
    #It will not use class name or object of that class , but called using class name.
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True

print('-------------------------------------------------------')

#calling alternative constructor
emp_1 = Employee.from_string('Jayashnakara-DM-10000')
emp_2 = Employee.from_string('Surya-DM-100000000')

print('--------------static method -------------------')

#Note: Better call using class name.

#call static method using class name
my_date = datetime.date(2019, 9, 15)
print(Employee.is_workday(my_date))

#call static method using object
print(emp_1.is_workday(my_date))

print('-------------class method -------------')

# Note : better use class name for calling

#call classmethod using class name
Employee.set_raise_ammount(1.90)
print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

#call using object name
emp_1.set_raise_ammount(2.1)
print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

print('----------- Regulor method -----')

#Note : Better call using object name.

#call using object name.
print(emp_1.getFullname())
print(emp_2.getFullname())

#call using class name
print(Employee.getFullname(emp_1))
print(Employee.getFullname(emp_2))







