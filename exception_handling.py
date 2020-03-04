"""
Exception handling:
try : Put code which possible throws some exception or code needs be handled for error

except : Specify the more specific exception and then more generic exception, "Exception" is more generic exception in python
         except Exception_type as e: => Means we are intersted in thrown exception
         except Exception: ==> Means we are intersted manual description about the exception by programer.

else: specify the code if there is no exception in try block which should need to run.

finally: specify code needs to be executed irrespective of the exception is occured or not. Like clean-up routines.

raise: used to generate custom exception
"""
#Example 1
try:
	#filename = "simple.txt"
	filename = "courrpet.txt"
	f = open(filename)
	if f.name == 'courrpet.txt':
		raise Exception
except FileNotFoundError:
	print("File is not able to open")
except Exception:
	print("something went wrong")
else:
	print("File is successful opend")
finally:
	print("File operations is successfull")
	f.close()


print("\n")
#Example 2

try:
	f = open("simple.txt")
	#v = bad_error
	raise FileNotFoundError
except FileNotFoundError as e:
	print("File not found exception")
	print(e)
except Exception as e:
	print(e)
else:
	print("Code which should follow after try block code in case if there is no exception")
finally:
	print("Execute this block always")
	f.close()
