class computer:

    def comDetails(self, ram, processor):
        self.ram = ram
        self.processor = processor
        print ("My computer details {}gb RAM and {} processor".format(self.ram, self.processor))


comp1=computer()
comp2=computer()

#Call using class name. In this case we need to pass the object to funtion.

computer.comDetails(comp1, 8, 'i5')
computer.comDetails(comp2, 8, 'i7')


# Call using object . In this case no need to pass object name as parameter. By default it will
# pass calling object as a first parameter.


comp1.comDetails(16, 'i5')
comp2.comDetails(18, 'i7')

