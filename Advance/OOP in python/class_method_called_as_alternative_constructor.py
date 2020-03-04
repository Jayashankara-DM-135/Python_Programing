
# class methos is also called as alternative constructor
  # It means inside the class method calling constructor/__init__ method to craete the objects.

  # Lets say we got employee details in one string. Now we have to extract employee detials like first name
  # last name and pay from that string and call the __init__ method to craete the objects.
  # This can be done using class method.

  # Inside class method we will parse the string and call the __init__ method from class method.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay

    def getFullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    # here 'from' it's just usaul way of naming alternative constructor.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        #Now call the __init__ method, like Empolyee(first,last, pay), But alreday we have class name in cls
        # use cls.
        #Here we are creating object and calling __init__ method.
        return cls(first, last, pay)


emp_1 = Employee.from_string("jayashakara-dm-1000")
emp_2 = Employee.from_string('surya-dm-1000000')

print(emp_1.getFullname())
print(emp_2.getFullname())

#call using class name
print(Employee.getFullname(emp_1))




