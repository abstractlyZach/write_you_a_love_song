# extract_artist_ngrams.py

# extracts all the artists from the batch files and then creates an n-gram 
# text for them in {project}/data/ngrams

import json
import os
from collections import defaultdict
import script_utils

# prompt user to fix the titles first 
import fix_titles

this_file = os.path.dirname(__file__)
batch_directory = os.path.join(this_file, '../data/songs/batch')
ngrams_directory = os.path.join(this_file, '../data/ngrams')

# get a set of artists 
batch_files = os.listdir(batch_directory)
artists = set()
for batch_file_name in batch_files:
	batch_file = os.path.join(batch_directory, batch_file_name)
	with open(batch_file, 'r', encoding='utf-8') as json_file:
		songs = json.load(json_file)
	for song in songs:
		artists.add(song['artist'])

print('Creating artist files.')
for artist in artists:
	# dictionary mapping ngrams (tuple) to counts of those tuples
	ngrams = defaultdict()
	print('   Creating file for {}...'.format(artist))
	artist_file_name = artist.replace(' ', '_') + '.txt'
	artist_ngrams_file = os.path.join(ngrams_directory, artist_file_name)
	with open(artist_ngrams_file, 'w', encoding='utf-8') as writefile:
		# scan through all batch files
		for batch_file_name in batch_files:
			batch_file = os.path.join(batch_directory, batch_file_name)
			with open(batch_file, 'r', encoding='utf-8') as json_file:
				songs = json.load(json_file)
			for song in songs:
				if song['artist'] == artist:
					verses = song['verses']
					for verse in verses:
						for line in verse:
							print(script_utils.line_to_ngrams(line, 2))

