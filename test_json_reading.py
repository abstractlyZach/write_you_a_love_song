# test_json_reading.py

import json
import sys

# with open('text.json', 'r', encoding='utf-8') as file:
# 	a = json.load(file)

# print(type(a))
# print(type(a[0]))

# for i in range(len(a)):
# 	print(a[i]['title'])
# 	print(a[i]['artist'])
# 	print(a[i]['text'])

# 	print()
# 	print('*' * 20 + "BEGIN LYRICS" + '*' * 20)
# 	print()
# 	for line in a[i]['text']:
# 		print(line)

# 	print()

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf-8') as file:
	a = json.load(file)

for i in range(len(a)):
	print()
	print('*' * 20 + "BEGIN LYRICS" + '*' * 20)
	print()
	print('ARTIST:')
	print('   ' + a[i]['artist'])
	print('TITLE:')
	print('   ' + a[i]['title'])
	print()
	# print(a[i]['verses'])
	verses = a[i]['verses']
	for verse in verses:
		for line in verse:
			print(line.strip())
		print()
	
	print()
	print('*' * 20 + "END LYRICS" + '*' * 20)
	print()