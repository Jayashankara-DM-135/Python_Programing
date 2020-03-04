class Employee:
    def __init__(self, first, last, pay):
        #below varibles is called instance varbile.
        # Means there value is differ object to object.
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jayashankara', 'DM', 1000)
emp_2 = Employee('Surya', 'DM', 100000)




print(emp_1.first)
print(emp_2.first)


#emp_1 is passed as a argument when it's called with object.
print(emp_1.fullname())

# object needs to be passed explicity when we are calling method which take object as a parameter.
print(Employee.fullname(emp_1))
