"""
"""
import csv

html_output = ''
names = []

with open('sample_csv.txt', 'r') as fr:
	csv_reader = csv.reader(fr)

	next(csv_reader)
	next(csv_reader)

	for line in csv_reader:
		if line[0] == 'RCB player':
			break
		names.append(f'{line[0]} {line[1]}')


html_output+=f'<p1> This are {len(names)} of CSK player </p1>\n'
html_output+="<ul>"
for name in names:
	html_output+=f'\n\t<li>{name}<\li>'
html_output +="\n</ul>"
print(html_output)



