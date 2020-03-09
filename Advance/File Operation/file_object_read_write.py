"""
File object: read and write files
"""

#By default it will open for read
# r -> read
# w -> write
# A -> append
# r+ -> read and write

print("------------------------ File opening normal way ------------------")
# if we open like this then , We have to close the file explicity
f = open('simple_text.txt', 'r')

print(f.name)
print(f.mode)

#file closing
f.close()


#context manager, with context manger we not need to close the file explicitly, context manager will take care of this.
print("-------- context manger way of opening file ------------------------")
with open('simple_text.txt', 'r') as fd:
	# read the full content of the file
	f_content = fd.read()
	#print("The file content is \n {}".format(f_content))
	print(f_content)

#At this stage file is closed automatically
print("--- outside ---")
print(fd.mode) #even those file is closed fd is still accessble , but we can't perform any action
print(fd.name) #same here
#print(fd.read()) #This is not possible since file already closed

print("-------------- reading file using readline------------------------")
with open('simple_text.txt', 'r') as fa:
	#reads one line at time
	# end='' : By defalut adds new line at the end of stament, by using end='' we can remove by defalut behaviour
	f_line = fa.readline()
	print(f_line, end='')

    #Now it prints second line , file pointer or descriptor will increment after all read.
	f_line = fa.readline()
	print(f_line, end='')

    #Now it prints second line , file pointer or descriptor will increment after all read.
	f_line = fa.readline()
	print(f_line)

print("-------------- reading file using readlines------------------------")

with open('simple_text.txt', 'r') as fb:
	#reads all the lines in file and print it as a list entry
	flines = fb.readlines()
	print(flines)


print("---------------------- use for loop to print each line ------------")

with open('simple_text.txt', 'r') as fp:
	for myline in fp:
		print(myline, end='')
 
print("-------------------How to print first 20 charcter from file -----------")
with open('simple_text.txt', 'r') as fq:
	content = fq.read(20)
	print(content, end='')

	#if we call again, It will read next 20 characters
	content = fq.read(20)
	print(content, end='')

	content = fq.read(20)
	print(content, end='')

	content = fq.read(20)
	print(content, end='')
	fq.seek(0) #set the file pointer to beging

    #When end of the file reached empty strimng will return
	content = fq.read(20)
	print(content, end='')
	print("\n")


print("----------------- 20 character can also read like this -------")

with open('simple_text.txt', 'r') as fm:
	content = fm.read(20)
	print(fm.tell()) #tells current file pointer position in file
	while len(content) > 0:
		print(content, end='')
		content = fm.read(20)

print("=================== Write operation ===============================")
# mode w : will overwite the file if it's already exist. to avoid overwrite use append mode (a->lower case)
with open('simple_text2.txt', 'w') as fw:
	fw.write("File write operation is done with all ")
	fw.seek(0)#starts from beging
	fw.write("Hello world ")


print("======================Copy from one file to anothe file ==============")

with open('simple_text.txt', 'r') as fr:
	with open('simple_text_output.txt', 'w') as fw:
		for line in fr:
			fw.write(line)

print("====================== image copying =====================================")
#to copy images we have to open a file in binary mode.

with open('RCB.jpg', 'rb') as fr:
	with open('Banglore.jpg', 'wb') as fw:
		for line in fr:
			fw.write(line)
