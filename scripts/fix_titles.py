# fix_titles.py

# interactive prompt that allows me to fix lyrics whose window titles
#     weren't standard, so I couldn't parse them.

import json
import os

this_file = os.path.dirname(__file__)
batch_directory = os.path.join(this_file, '../data/songs/batch')
batch_files = os.listdir(batch_directory)

fix_counter = 0

for batch_file_name in batch_files:
	batch_file = os.path.join(batch_directory, batch_file_name)
	with open(batch_file, 'r', encoding='utf-8') as json_file:
		songs = json.load(json_file)

	# # write to a new file
	# new_file_name = os.path.join(batch_directory, 'new_' + batch_file_name)

	# overwrite old file
	new_file_name = batch_file
	song_list = []
	with open(new_file_name, 'w', encoding='utf-8') as new_json_file:
		for song in songs:
			# extract data for song
			title, artist, verses = song['title'], song['artist'], song['verses']
			if song['artist'] == 'fix please':
				fix_counter += 1
				# print whole title string for user input
				print(song['title'])
				# get user input for new title and artist
				title = input("New title: ")
				artist = input("New artist: ")
				print()
			song_dict = {
				'title': title,
				'artist': artist,
				'verses': verses
			}
			song_list.append(song_dict)
		# dump song list to the file
		json.dump(song_list, new_json_file, indent=0)

print('{} songs fixed.'.format(fix_counter))