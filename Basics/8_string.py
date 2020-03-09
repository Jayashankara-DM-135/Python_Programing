"""
This file contanis all the funcations and propertice related to string
"""

#declare the string
mes = "Hellopython, wellcom to IT"
mes1 = "Hello python, You are beauty"
mes2 = """Hello python,
          Thanks """

print(mes)
print(mes1)
print(mes2)

print("========================================================")
#Just add empty line
print("\n")

#string slicing
#Note: second index is excluded
print(mes[0])
print(mes[0:5])
print(mes[:8])
print(mes[6:])

print("=============== 1 ==========================================")
#methods are help full for debugging
print(help(str)) #list out all the methods and attributes assoicated with string data type str
print(dir(mes)) #list out methods and attributs assoicated with mes
print(help(str.lower))

print("=================2 ========================================")
#methods
print(mes.upper())
print(mes.lower())
print(mes.find("python"))
print(mes.count("python"))
print(mes)

msg = "Hello world"
#Replace is not inplace, Hence it's  stored in separte
replace = mes.replace("Hello", "Hi")

print (replace)


print("*****************************4 ***********************************")
#fstring pyhon 3.6 and grater

fname = "Jayashankara"
lname = "DM"

print("{} {}".format(fname.upper(), lname))
#also using f stream we can write it like this.
print(f"{fname} {lname}")
print(f"{fname.upper()} {lname.upper()}")



