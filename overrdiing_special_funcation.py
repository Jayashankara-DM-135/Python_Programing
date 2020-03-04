"""
Special funcations overloading.
-----------------------------
It's similar to c++ operator overloading
"""

class Empolyee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def getFullname(self):
        return "{} {}".format(self.first, self.last)

    def __add__(self, other):
        if (isinstance(other, Empolyee)):
                return self.pay + other.pay

    def __repr__(self):
        return "employee({} , {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} -> {}".format(self.getFullname(), self.email)

    def __len__(self):
        return len(self.first + self.last)



emp1 = Empolyee("Jayashankara", "DM", 1000)
emp2 = Empolyee("Suresh", "Raina", 5000)
"""
It will invoke in below order:
1> __str__ if it's overloaded first
2> __repr__ if it's overloded and __str__ is not overloaded
3> otherwise it prints vage info about object

"""
print(emp1)

# We can call this methods like this as well
print(emp1.__str__())
print(emp1.__repr__())
print(Empolyee.__str__(emp1))

# We can also call another way as well
print(str(emp1))
print(repr(emp1))

#Now uses overloaded len method
print(emp1.__len__())
print(len(emp1))

#Now use overloaded add method to add pay of two empolyee
print(emp1 + emp2)
#also we can call using class name
print(Empolyee.__add__(emp1, emp2))
print(emp1.__add__(emp2))





