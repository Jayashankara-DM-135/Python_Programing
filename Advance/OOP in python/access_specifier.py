class Employee:
    __ecount = 0
    _called = 1

    def increment(self):
        self.__ecount +=1
        print(self.__ecount)

Emp1 = Employee()
Emp1.increment()
Emp1.increment()

Emp1.__ecount = 10
Emp1._called = 4
Emp1.increment()
print(Emp1._Employee__ecount)

print(dir(Emp1))
