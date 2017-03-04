# datasetmetrics.py

import json
from nltk import word_tokenize

def get_average_tokens(json_file_name):
	'''Returns the average number of tokens per song in a collection of songs
	stored in a json file.'''
	song_counter = 0
	token_counter = 0
	with open(json_file_name, 'r', encoding='utf-8') as song_file:
		songs = json.load(song_file)
	for song in songs:
		token_counter += count_tokens(song['verses'])
		song_counter += 1
	return token_counter / song_counter

def count_tokens(song):
	'''Counts the tokens in a song. Song is passed in as a list of verses'''
	token_count = 0
	for verse in song:
		for line in verse:
			token_count += len(word_tokenize(line))
	return token_count