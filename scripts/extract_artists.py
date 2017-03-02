# extract_artists.py

# cleans the artist folder, then
# extracts all of the artists from the batch folder and creates artist files for them

import json
import os

# prompt user to fix the titles first 
import fix_titles

this_file = os.path.dirname(__file__)
batch_directory = os.path.join(this_file, '../songs/batch')
artist_directory = os.path.join(this_file, '../songs/artists')

# delete old artist files
print('Cleaning artist/ directory...')
artist_files = os.listdir(artist_directory)
remove_counter = 0
for file in artist_files:
	print("   Removing: " + file)
	os.remove(os.path.join(artist_directory, file))
	remove_counter += 1
print("Removed {} files from the artists/ directory.".format(remove_counter))

# create new artist files
batch_files = os.listdir(batch_directory)
artists = set()
for batch_file_name in batch_files:
	batch_file = os.path.join(batch_directory, batch_file_name)
	with open(batch_file, 'r', encoding='utf-8') as json_file:
		songs = json.load(json_file)
	for song in songs:
		artists.add(song['artist'])

# run another pass through for each artist
print('Creating artist files...')
for artist in artists:
	print('   Creating file for {}...'.format(artist))
	song_list = []
	artist_file_name = artist.replace(' ', '_') + '.json'
	artist_file = os.path.join(artist_directory, artist_file_name)
	# create a file for each artist
	with open(artist_file, 'w', encoding='utf-8') as writefile:
		# scan through all batch files
		for batch_file_name in batch_files:
			batch_file = os.path.join(batch_directory, batch_file_name)
			with open(batch_file, 'r', encoding='utf-8') as json_file:
				songs = json.load(json_file)
			# add the songs that were written by them	
			for song in songs:
				if song['artist'] == artist: 
					song_dict = {'title': song['title'], 'artist': song['artist'], 
						'verses': song['verses']}
					song_list.append(song_dict)
		# json dump to that artist's file
		json.dump(song_list, writefile)

print('Created {} artist files.'.format(len(artists)))