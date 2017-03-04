# utils.py

import json
import os

def get_song(index):
	to_return = ''
	with open('data/songs/batch/top_artists.json', 'r', encoding='utf-8') as json_file:
		songs = json.load(json_file)
	song = songs[index]
	to_return += '<h3>ARTIST:</h3>'
	to_return += song['artist'] + '<br>'
	to_return += '<h3>TITLE:</h3>'
	to_return += song['title'] + '<br>'
	to_return += '<br><br>'
	verses = song['verses']
	for verse in verses:
		for line in verse:
			to_return += line + '<br>'
		to_return += '<br>'
	return to_return

def get_artist_songs(artist):
	'''Returns a list of song names from an artist. 
	Empty list if the artist can't be found.'''
	song_list = []
	batch_directory = 'data/songs/batch'
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
	batch_directory = 'data/songs/batch'
	batch_files = os.listdir(batch_directory)
	for batch_file_name in batch_files:
		batch_file = os.path.join(batch_directory, batch_file_name)
		with open(batch_file, 'r', encoding='utf-8') as json_file:
			songs = json.load(json_file)
		for song in songs:
			if song['title'].strip().lower() == song_title.strip().lower():
				return song['verses']
	return None

def get_bad_words():
	'''Returns a list of bad words to avoid'''
	with open('/data/wordlists/google_bad_words', 'r', encoding='utf-8') as json_file:
		bad_words = json.load(json_file)
	return bad_words

