# print_songs.py

import json
import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf-8') as file:
	songs = json.load(file)

for i in range(len(songs)):
	print()
	print('*' * 20 + "BEGIN LYRICS" + '*' * 20)
	print()
	print('ARTIST:')
	print('   ' + songs[i]['artist'])
	print('TITLE:')
	print('   ' + songs[i]['title'])
	print()
	# print(a[i]['verses'])
	verses = songs[i]['verses']
	for verse in verses:
		for line in verse:
			print(line.strip())
		print()
	
	print()
	print('*' * 20 + "END LYRICS" + '*' * 20)
	print()
print("Printed {} songs.".format(len(songs)))
print()