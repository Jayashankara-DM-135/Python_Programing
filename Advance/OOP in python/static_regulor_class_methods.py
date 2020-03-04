# 1> Regulor method takes first argumet as object automatically.
#    where as classmethods takes first argiument as class automatically.

# 2> Regular method usally called with objects , But it's also possible to call using class name. When we are
#    using class name we should explicity pass object as firsr paramter.
     # where as class methods usally called using class name , but it's also possible call using object, But in this
     # case no need to pass class as a first parameter .parameter

  # 3> class method defined using @classmethods tag


class Employee:
    no_of_employee = 0
    raise_ammount = 1.04

    #Regulor or normal method. which take first parameter as object.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = last+'.'+last+'@gmail.com'
        self.pay = pay

        Employee.no_of_employee += 1

    def getFullName(self):
        return '{} {}'.format(self.first, self.last)

    # class method , which takes class as a parameter
    @classmethod
    def set_raise_ammout(cls, ammount):
        cls.raise_ammount = ammount


emp_1 = Employee('Jayashankara', 'DM', 10000)
emp_2 = Employee('Surya', 'DM', 10003)

# Usual way of calling
#call normall method using object.
print(emp_1.getFullName())

#call using class name
print(Employee.getFullName(emp_1))




print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_1.raise_ammount)
# Usual way of calling class method using class name.
Employee.set_raise_ammout(10)

print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_1.raise_ammount)


#call using object name, but no need to pass class name as a first parameter .
# sicne with object name python internally can determine the class using object.

emp_1.set_raise_ammout(11)
# Note: In above line even those we called class method via object. Inside the method class varible is accesed
#       using the class name, Hece chamges is reflected for all object and class. It means emp_1 will not have
#       'raise_ammount' attribute in it's namespace.

print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_1.raise_ammount)





