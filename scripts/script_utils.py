# script_utils.py

# utilities for the scripts directory

import nltk
from nltk.tokenize.moses import MosesDetokenizer

def keep_line(line):
	'''Returns a boolean telling whether or not to keep a line from the ngrams file'''
	to_return = True
	# # remove lines with '_' in them because lines with '_' have POS tags,w 
	# if '_' in line:
	return True

UNWANTED_PUNCTUATION = ['(', ')', '"', "``", "''"]
def line_to_ngrams(line, n, punctuation=False):
	'''Processes the line and returns a list of n-grams.
	If punctuation is True, then punctuation will be counted as tokens.'''
	ngrams = []
	if punctuation:
		words = nltk.word_tokenize(line.lower())
	else:
		words = line.lower().split()
		# maybe manually strip out .?!:;
	for punctuation in UNWANTED_PUNCTUATION:
		while punctuation in words:
			words.remove(punctuation)
	# add start and end delimiters to the words
	words = ['<S>'] + words + ['</S>']
	for start_index in range(len(words) - n + 1):
		ngrams.append(tuple(words[start_index: start_index + n]))
	return ngrams

detokenizer = MosesDetokenizer()
def detokenize(words):
	return ' '.join(detokenizer.detokenize(words))