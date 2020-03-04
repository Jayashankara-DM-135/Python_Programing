class Empolyee:
    hikeRate = 1.01
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def getFullname(self):
        return "{} {}".format(self.first, self.last)
    
    @classmethod
    def setHikerate(cls, ammount):
        cls.hikeRate = ammount
        
    
    def getHike(self):
        return int(self.pay * self.hikeRate)
    
class Developer(Empolyee):
    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first,last,pay)
        """
        Above staments can be implemented as below, But above one is prefered one.
        Empolyee.__init__(self, first, last, pay)
        """
        self.prog_lang = prog_lang

class Manager(Empolyee):
    def __init__(first, last, pay, empolyees=None):
        super(Manager, self).__init__(first, last, pay)
        if self.empolyees is None:
            self.empolyees = []
        else:
            self.empolyees = empolyee
    
    def addEmp(self, emp):
        if emp not in self.empolyees:
            self.empolyees.append(emp)
    
    def removeEmp(self, emp):
        if emp in self.empolyees:
            self.empolyees.remove(emp)
        else :
            print("Empolyee is not exist" + emp)
    
    def print_employees(self):
        for emp in self.empolyee:
            print(emp.getFullname())
    
    


# Helpfull debug prints
'''
print(help(dev1)) 
print(dev1.__dict__)
print(Empolyee.__dict__)
'''


dev1 = Developer("Jayashnakara", "DM", 1000, "Java")
dev2 = Developer("Rain", "Suresh", 2000, "python")

man1 = Manager("Dohini", "Singh", 10000, "All")

man1.addEmp(dev1)
man1.addEmp(dev2)

print(man1.print_employees())

man1.removeEmp()

print(man1.print_emloyees())

"""
isinstance: Will check first parameter is instance of second parameter.
issubclass: Will check first parameter is subclass of second parameter.
"""
print(isinstance(dev1, Developer)) #TRUE
print(isinstance(dev1, Employee))  #False

print(issubclass(Developer, Empolyee)) # TRUE
print(issubclass(Developer, Manager)) #False


