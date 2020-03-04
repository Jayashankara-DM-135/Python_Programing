"""
OS module usage:
"""
import os

#List out all the method and attributes related to os module
print(dir(os))

#Display current working day
print(os.getcwd())

#change the directory
#os.chdir('/Users/1000259555/Desktop/Python')

print(os.getcwd())

#List out all the files in current directory

print(os.listdir())

#Create the first-level directory in current working director
#if already created then it will through error
#os.mkdir("OS-DEMO-EXAMPLE")
#os.rmdir("OS-DEMO-EXAMPLE")
#if we want create more than two level of directory or even single level as well
#if already created then it will through error
#os.makedirs("Fist-Lvel/Second-level")

# Deletes directory recursively, Means all the directory
#os.removedirs("Fist-Lvel/Second-level")

# Delectes only Second-level dir or inner-most directory
#os.rmdir("Fist-Lvel/Second-level")


print(os.listdir())

#os.rename('Banglore.jpg', 'Banglore_RCB.jpg')
print(os.listdir())

print(os.stat('simple.txt'))
print(os.stat('simple.txt').st_size)
print(os.stat('simple.txt').st_atime)


#print st_atime in human readble format
from datetime import datetime
mod_time = os.stat('simple.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print("-------------------- List all the directoires and file from spcified path recursively-----------")

for dirpath, dirname, filename in os.walk('/Users/1000259555/Desktop/Python'):
	print('Current path:', dirpath)
	print('Current Dirname:', dirname)
	print('File names:', filename)


print("--------------------- List out environmental varibales ----------------")
#List out all environment
print(os.environ)

#list only sepfic environment varible
print("\n\n")
print(os.environ.get('HOME'))

print("------------------------- combine the file path with home dir-----------")

#It is just prepare the path, but creates the files
#file_path = os.path.join(os.environ.get('HOME'), 'simple.txt')
#print(file_path)

#Check basename. dirname and split the dir and file name, of the file path
# these three methods works on even those path does not exist in computer, just specifying fake path is enough
print(os.path.basename('/user/tmp.txt'))
print(os.path.dirname('/usr/tmp.txt'))
print(os.path.split('/usr/tmp.txt'))

#Now check file path is exist or not
print(os.path.exists('/usr/tmp.txt'))

#Check it's directory or not
print(os.path.isdir('/usr/ggggg'))

#check it's file or not
print(os.path.isfile('/usr/tmp.txt'))

#extract file path and extenstion
print(os.path.splitext('/usr/tmp.txt'))


#what all are avilable in os.path
print(dir(os.path))


