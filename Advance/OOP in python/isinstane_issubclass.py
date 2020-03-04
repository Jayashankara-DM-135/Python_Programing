# isinstance(obj, classname): will check obj is instance of provided class, if it's yes, It will return True otherwise False.

# Note: if object is subclass object and class is parenet , In this case as well isinstance(obj, parenetclass) returns
# True.

# issubclass(aclass, bclass): check aclass is subclass of bclass or not.
#if it's yes, then returns True otherwise False.

class Employee:
    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def getFullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise_ammount(self):
        return self.pay * self.raise_ammount

    @classmethod
    def set_raise_ammount(cls, ammount):
        cls.raise_ammount = ammount

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True


#you can use this as well Employee.__init__(self, first, last, pay) to call base class __init__ method
#This is better in case of multiple inheritenace.

class Developer(Employee):
    raise_ammount = 1.05
    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lan = prog_lan

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = None
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.getFullname())


dev_1 = Developer('Jayashankara', 'DM', 1000, 'Python')
dev_2 = Developer('Surya', 'DM', 10000, 'Java')

emp_1 = Employee('Savitha', 'DM', 1000)
emp_2 = Employee('Poornima', 'C', 24000)
emp_3 = Employee('Manvith', 'CD', 1)

man_1 = Manager('John', 'Hegton', 199999, [emp_1, emp_2])


print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))
print(isinstance(emp_1, Manager))
print(isinstance(emp_1, Employee))

print('------')

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Employee, Manager))
print(issubclass(Employee, object)) # object class is super class of all.




