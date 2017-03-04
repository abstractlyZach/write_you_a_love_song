# utils.py

import json
import os

def get_artist_songs(artist):
	'''Returns a list of song names from an artist. 
	Empty list if the artist can't be found.'''
	song_list = []
	batch_directory = '../songs/batch'
	batch_files = os.listdir(batch_directory)
	for batch_file_name in batch_files:
		batch_file = os.path.join(batch_directory, batch_file_name)
		with open(batch_file, 'r', encoding='utf-8') as json_file:
			songs = json.load(json_file)
		for song in songs:
			if song['artist'].strip().lower() == artist.strip().lower():
				song_list.append(song['title'])
	return song_list

def get_lyrics(song_title):
	'''Returns a list of verses for the song with the given title.'''
	batch_directory = '../songs/batch'
	batch_files = os.listdir(batch_directory)
	for batch_file_name in batch_files:
		batch_file = os.path.join(batch_directory, batch_file_name)
		with open(batch_file, 'r', encoding='utf-8') as json_file:
			songs = json.load(json_file)
		for song in songs:
			if song['title'].strip().lower() == song_title.strip().lower():
				return song['verses']
	return None