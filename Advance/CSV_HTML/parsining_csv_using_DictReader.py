"""
"""
import csv

html_output = ''
names = []

with open('sample_csv.txt', 'r') as fr:
	csv_reader = csv.DictReader(fr)

	next(csv_reader)

	for line in csv_reader:
		if line['fname'] == 'RCB player':
			break
		names.append(f"{line['fname']} {line['lname']}")
	

html_output+=f'<p1> There are {len(names)} in CSK tean </p1>\n'
html_output+='<ul>'

for name in names:
	html_output+=f'\n\t<li>{name}</li>'

html_output+='\n</ul>'

print(html_output)
