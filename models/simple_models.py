# simple_models.py

import random
from . import unigrams
from . import bigrams
from utils import song
from utils import exceptions
from utils import get_data
from utils import text, constants
from . import basic_songwriter

class GoogleNGramsSongWriter(basic_songwriter.BasicSongWriter):
	def __init__(self, artist):
		self._artist = artist

	def new_song(self, short=False):
		return simple_song(self._artist, short=short)


def string_bigrams(seed_word, len=10):
	'''Strings together bigrams for the given length.'''
	current_word = seed_word
	string_sequence = [current_word]
	for i in range(1, len):
		try:
			current_word = bigrams.get_next_word(current_word)
		except exceptions.WordNotFoundError:
			if constants.DEBUG_ON:
				print('inserting unigram because of {}'.format(current_word))
			current_word = unigrams.get_word()
		string_sequence.append(current_word)
	return ' '.join(string_sequence)


def simple_song(artist, short=False):
	'''Reads a random song from an artist and then creates lines using bigrams
	(seeded with the first word of every line of the original) to write a song.'''
	final_song = []
	# Get a random song title from the artist
	artist_songs = get_data.get_artist_songs(artist)
	if len(artist_songs) > 0:
		selected_song_title = random.choice(artist_songs)
	else:
		raise exceptions.ArtistNotFoundError(artist)
	# Get the lyrics to the random song
	selected_song = get_data.get_lyrics(selected_song_title)
	# Write the generated song
	for verse_index, verse in enumerate(selected_song):
		if short and verse_index >= 3:
			break
		final_song.append([])
		for line in verse:
			# use the first word of the original song as the seed word
			seed_word = line.split()[0]
			# write a generated string that's the same length as the original line
			final_song_line = string_bigrams(seed_word, len=len(line.split()))
			final_song[verse_index].append(final_song_line)
	return song.Song(selected_song_title + ' (Remix) (kinda)', 
						artist.title() + " (and Zach)", 
						final_song
					)

# def get_artist_line_from_bigrams(length=10):
# 	current_word = '<S>'
# 	string_sequence = []
# 	artist_bigrams, enders = bigrams.get_bigram_generator_and_enders('data/ngrams/Taylor_Swift.txt')
# 	while len(string_sequence) <= length:
# 		try:
# 			previous_word = current_word
# 			current_word = bigrams.get_next_word(previous_word, bigrams=artist_bigrams)
# 			while current_word == '</s>':
# 				current_word = bigrams.get_next_word(previous_word, bigrams=artist_bigrams)
# 			if len(string_sequence) == length - 1:
# 				if current_word not in enders:
# 					continue
# 		except exceptions.WordNotFoundError:
# 			if constants.DEBUG_ON:
# 				print('inserting unigram because of {}'.format(previous_word))
# 			current_word = unigrams.get_word()
# 		string_sequence.append(current_word)
# 	string_sequence.insert(0, '<S>')
# 	string_sequence.append('</S>')
# 	return text.detokenize(string_sequence)