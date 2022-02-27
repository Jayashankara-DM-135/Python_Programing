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

Note: Don't use final blcok for cleanup file which you opened in try blcok.
	Ex:
          if file opening in try block is thrown excpetion due to file not found, then later in finally block if you are trying close the file it will error out.
	  So closing file should be done at else block , But final block is used do other cleanup, but not file close.

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

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("\n")
#Example 2

try:
	f = open("simple.txt")
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
	f.close()  # This will give errror if there is exception from try block.
=============

try:
	f = open("simple.txt")
	raise FileNotFoundError 
except FileNotFoundError as e:
	print("File not found exception")
	print(e)
except Exception as e:
	print(e)
else:
	print("Code which should follow after try block code in case if there is no exception")
	# do other stufs 
	f.close()  # This works because 'else' blcok will execute only when there no exception.
finally:
	print("Execute this block always")
	

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Why this is not a good way writing exception handling code ?
We should be handling one specific exception using try/exeption/else/finally blcoks.

Even those below code works fine, There are 4(open, write, read and close) source of exception we are hadning in same  try/exeption/else/finally blcoks, this not recommended 

try:
	f = open("simple.txt")
	raise FileNotFoundError 
	f.write("some content")
	print(f.read())
	f.close()
except FileNotFoundError as e:
	print("File not found exception")
	print(e)
except Exception as e:
	print(e)
else:
	print("Code which should follow after try block code in case if there is no exception")
finally:
	print("Execute this block always")
	

