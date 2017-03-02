# test_csv_reading.py
import csv

print('=' * 15 + ' BEGIN ' + '=' * 15)

with open('text.csv', encoding='utf-8') as csv_file:
	reader = csv.DictReader(csv_file)
	for row in reader:
		print(row)
		print(row['title'])
		print('by ' + row['artist'])
		for line in row['text']:
			print(line)
		print()