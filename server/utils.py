# utils.py

import json

def get_song(index):
	to_return = ''
	with open('../songs/batch/top_artists.json', 'r', encoding='utf-8') as json_file:
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
