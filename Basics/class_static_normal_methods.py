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
It's called using class name or object name.

================
 Normal method:
 Methods which are not defined using "@staticmethod or @classmethod"
 These methods takes object as parameter.
 Its called using object or class method. if called using class name then class name is not implicitly passed to method.

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
        print("Raise method is called")
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


if __name__ == '__main__':
    empstr1 = "Jayashankara-DM-100"
    empstr2 = "Suresh-Raina-1000"
    emp1 = Empolyee.from_string(empstr1)
    emp2 = Empolyee.from_string(empstr2)


    print(emp1.first)
    print(emp2.second)

    print(emp1.getFullName())
    print(emp2.getFullName())

    #call classmethod using object.
    print("======")
    emp1.raise_salary(1.8)
    print(emp1.hike)
    print(emp2.hike)
    print(Empolyee.hike)

    print("======")
    my_date = datetime.date(2016, 7, 6)

    # static method can be called using object or class name.
    # Baiscally it's not a good idea to call using object. Since static methods doesn't accept class or object as parameter.
    # if you use object for calling static method , then it will pass calling object as a parameter to static method.
    print(emp1.isWorkday(my_date))
    print(Empolyee.isWorkday(my_date))

    # Normal method called using class name.But here we have to pass the object explicity.
    # If normal method called using object, then no need to pass the object and it's implicity passed by python.
    print(Empolyee.getFullName(emp1))



