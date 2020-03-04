class computer:
    def __init__(self, ram, processor):
        print('Init methos is called for object with address {}'.format(id(self)))
        self.ram =ram
        self.processor = processor


    def compDetails(self):
        print("My computer details: {}gb RAM and {} processor".format(self.ram, self.processor))



#While creatating object, python will by default calls __init__ method.`.

comp1 = computer(8, 'i3')
comp2 = computer(16,'i7')


# Now try to call the compDeatils using class name.
#When we call the method using class name , We have to pass the object for which method is invoked.
computer.compDetails(comp1)
computer.compDetails(comp2)

# Now try to call using object name. In this case no need to pass object as parameter.
# Python will by defalut takes calling object as a first parameter.

comp1.compDetails()
comp2.compDetails()



