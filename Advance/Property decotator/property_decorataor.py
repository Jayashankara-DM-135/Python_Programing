class Employee:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)


    def display(self):
        print(f' first:{self.first} \n last:{self.last} \n fullname:{self.fullname} \n email:{self.email}')


emp1 = Employee('JAI', "SHANKAR")
emp1.display()

emp1.fullname = "Surya Kumar"
emp1.display()
