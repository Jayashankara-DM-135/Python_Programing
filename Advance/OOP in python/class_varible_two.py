class Employee:
    no_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay
        # Here access class varible via class name rather than object, Since this varible is very common
        # to every object. There is nothing specific to objects. So use class name.
        Employee.no_of_employee += 1


print(Employee.no_of_employee)

emp_1 = Employee('Jeevan', 'CD', 1000)
emp_2 = Employee('Manvith', 'CD', 10000)

print(Employee.no_of_employee)


