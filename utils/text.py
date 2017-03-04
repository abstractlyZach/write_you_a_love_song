# text.py

from . import get_data

BAD_WORDS = get_data.get_bad_words()
def check_word(word):
	'''Returns true if the word is OK to use.'''
	return word in BAD_WORDS