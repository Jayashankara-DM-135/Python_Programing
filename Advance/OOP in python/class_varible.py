# class varibles are same for all the objects
# where as instance varible differ objects to objects.

# Note:
# Class varible can not be accessed directely. Need to access via object or class name.

# When class varible is accesed via object. Then python looks at that attribute/varible in following order
# 1> checks if that object has attribute (i mean it's instance varible or not)
# 2> otherwise, Looks for class vraible of that class .
# 3> otherwise , Looks for class which are inherited by this class have this class varible or not.


# if class varible is modified by using class name, then this changes is applicable to all objects.
# if class variable is modified by using object, then this changes is only applicable for that object.
#  not for all other objects.



class Employee:
    #class varible
    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        #instance varible
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay

    def apply_raise(self):
        #inside the method if you want to access the Class varible
        # better to access via objec rather than using class name.
        # Since some times outside of the class, class varible are modified using object
        # in this case whatever changes are made to class varible is only applicable to object which is
        # used to modify the class varibles.

        # It means once class varible is accessed via object , from then class vraible will be part of
        # namespace of the object.
        return self.pay * self.raise_ammount


emp_1 = Employee("Jayashankara", "DM", 1000)
emp_2 = Employee("Surya", "DM", 100000)

#Check the namesapce of class and objects
# class namespace : It contins raise_ammount attribute.
print(Employee.__dict__)
print('---------')
# emp_1 object namespace: Now it does not contain 'raise_ammount' attribute.
print(emp_1.__dict__)
#simillorly for emp_2 object
print('----------')
print(emp_2.__dict__)

print('++++++++++++++++++')
# Now try to access class varible
print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)


print('+++++++++++++++++++')
#Again check the name space for class and object. After just reading class varible via class name and object.

#Just reading class varible via object will not make , class varible to be part of object namespace.
#if we changes class varible values via object then only that class varible will be part of the object namespace.

print(Employee.__dict__)

print('-------')
print(emp_1.__dict__)
print('--------')
print(emp_2.__dict__)

print("+++++++++++++++")

#Now chnage class vaible via object.

# chnages only applied to object emp_1 and Now 'raise_ammount' part of emp_1 namespace, But not yet for emp_2 object.
emp_1.raise_ammount = 1.05

print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

print(Employee.__dict__)
print('--------')
print(emp_1.__dict__)
print('--------')
print(emp_2.__dict__)

print("++++++++++++++++++++")
# Now lets try chaning via class name

# This time onward whatever changes made to class varible via class name will not change
# emp_1 object 'raise_Ammount' sicne emp_1 object has this vailbe in it's namespace now.
Employee.raise_ammount = 1.07
print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print(Employee.apply_raise (emp_1))
print(emp_1.apply_raise())
print(emp_2.apply_raise())


