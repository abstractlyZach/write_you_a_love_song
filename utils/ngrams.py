# ngrams.py

# utility functions for ngrams

import nltk
import os
from . import constants

def process_line(line, n, punctuation=False):
	'''Processes the line and returns a list of n-grams.
	If punctuation is True, then punctuation will be counted as tokens.'''
	ngrams = []
	if punctuation:
		words = nltk.word_tokenize(line.lower())
	else:
		words = line.lower().split()
		# maybe manually strip out .?!:;
	# add start and end delimiters to the words
	words = ['<S>'] + words + ['</S>']
	for start_index in range(len(words) - n + 1):
		ngrams.append(words[start_index: start_index + n])
	return ngrams

def get_ngram_file_path(n, file_name):
	'Returns the ngram file path'
	return os.path.join(constants.NGRAMS_DIRECTORY, str(n), file_name)
