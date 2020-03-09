"""
CSV module: uses existing csv module to parse and update the CSV file.
"""

import csv

with open('name.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	#Contains all the contents
	print(csv_reader) #prints object adress

	for line in csv_reader:
		print(line) # print out line by line
	
	csv_file.seek(0) #reset the file pointer to beging of the file.
	for line in csv_reader:
		print(line[2]) #prints only thrid colum in CSV file
	
	csv_file.seek(0)
	for line in csv_reader:
		print(line[0])
	
	#Lets remove title name 
	csv_file.seek(0)
	next(csv_reader) #increments to next line
	
	print("----------After removing title--------------------")
	for line in csv_reader:
		print(line[0])

   

print("----- copy from one CSV file to onother CSV file-----")
with open('name.csv', 'r') as csv_fr:
	csv_reader = csv.reader(csv_fr)

	with open('new_name.csv', 'w') as new_fw:
		csv_writer = csv.writer(new_fw, delimiter='\t')
		for line in csv_reader:
			csv_writer.writerow(line)


print("----------- Read newly created csv file ----------------")
with open('new_name.csv', 'r') as new_fr:
	csv_reader = csv.reader(new_fr)

	for line in csv_reader:
		print(line)

print("------------- Specifying delimiter -------------------------")
with open('new_name.csv', 'r') as new_fr:
	csv_reader = csv.reader(new_fr, delimiter='\t')

	for line in csv_reader:
		print(line)



"""
Dictionary reader and writer used to read CSV file data.
with DictReader and DictWriter , Filed name will became keys 
"""

with open('name.csv', 'r') as csv_fr:
	csv_reader = csv.DictReader(csv_fr)

	for line in csv_reader:
		print(line)
	
	with open('new_name_dic.csv', 'w') as new_fw:
		filednames = ['name', 'id', 'age']
		csv_writer = csv.DictWriter(new_fw, fieldnames=filednames, delimiter='\t')

		csv_writer.writeheader() #it writes fieldnames as title
		for line in csv_reader:
			csv_writer.writerow(line)


print("===== Lets update only part of the csv file i mean left out soem cloums====================")

with open('name.csv', 'r') as csv_fr:
	csv_reader = csv.DictReader(csv_fr)

	for line in csv_reader:
		print(line)


	with open('new_dict.csv', 'w') as csv_fw:
		fieldnames =['name', 'id']
		csv_writer = csv.DictWriter(csv_fw, fieldnames=fieldnames, delimiter='\t')
		csv_writer.writeheader()
		for line in csv_reader:
			del line['age']
			csv_writer.writerow(line)

