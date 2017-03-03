# simple_models.py

import bigrams

def string_bigrams(seed_word, len=10):
	'''Strings together bigrams for the given length.'''
	current_word = seed_word
	string_sequence = [current_word]
	for i in range(1, len):
		current_word = bigrams.get_next_word(current_word)
		string_sequence.append(current_word)
	return ' '.join(string_sequence)

