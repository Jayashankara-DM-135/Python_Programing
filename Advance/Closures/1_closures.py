"""
Closures: 
          Python Closures are these inner functions that are enclosed within the outer function. 
          Closures can access variables present in the outer function scope.
"""
print('------------ Example 1----------------------')
def outer():
	msg = "Hi ABD"
    #At this stage print(msg) is prepared for inner function, But it will excute untill inner() is called,
    #Hence inner function having a access to msg"""
	def inner():
		print(msg)
	return inner()

outer()

print("------------- Example 2 ---------------------")

def outer1(msg1):
	def inner1(msg2):
		print("{0} {1}".format(msg1, msg2))
	return inner1

tfun1 = outer1("Hi")
tfun2 = outer1("Hello")

tfun1("ABD")
tfun2("Virat")





