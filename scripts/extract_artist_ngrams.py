# extract_artist_ngrams.py

# extracts all the artists from the batch files and then creates an n-gram 
# text for them in {project}/data/ngrams

# you must run this script from the main project directory

import json
import os
from collections import defaultdict
import script_utils
import sys

# prompt user to fix the titles first 
import fix_titles

# set n according to command line parameter
n = int(sys.argv[1])

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
	ngram_dict = defaultdict(int)
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
							ngrams = script_utils.line_to_ngrams(line, n, punctuation=True)
							for ngram in ngrams:
								ngram_dict[ngram] += 1
		# write the counts to the file
		for ngram, count in sorted(ngram_dict.items(), key=lambda x: x[1], reverse=True):
			to_write = ''
			for word_count in range(n):
				to_write += '{} '.format(ngram[word_count])			
			to_write += '\t' + str(count) + '\n'
			writefile.write(to_write)



