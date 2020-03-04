"""
Demostrate Property decorator:
1> Setter
2> Getter
3> deleter
"""

class Empolyee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

@fullname.setter
    def fullname(self, name):
    first, last = name.split(" ")
        self.first = first
        self.last = last

@fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

emp1 = Empolyee("Jayashnakra", "DM")
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

emp1.first = "Savitha"
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


# Now assign  fullname, It show error if we don't have setter method for this.
# Since we don't have any attribute called fullname. We have fullname method that
# is used as a attribute using property decorator.

# With help of fullname.setter we can assign the string to fullname
emp1.fullname = "Suresh Raina"
print #Create new line
print
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


#Now delete fullname will it invoke deleter decorator
del emp1.fullname
print ("***********")
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)






