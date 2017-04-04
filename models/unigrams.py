# unigrams.py

import numpy
import csv
from utils import text
import random

def read_unigrams(file_name='data/ngrams/1/count_1w.txt'):
	'''Reads a file of unigrams and their counts and returns a tuple
	containing a list of words and a list of their corresponding probabilities
	'''
	counts = []
	words = []
	with open(file_name, 'r') as tsvfile:
		reader = csv.reader(tsvfile, delimiter='\t')
		for unigram, count in reader:
			count = int(count)
			word = unigram.lower()
			counts.append(count)
			words.append(word)
	N = sum(counts)
	probabilities = [count / N for count in counts]		
	return (words, probabilities)


UNIGRAMS = read_unigrams()
def get_word(unweighted=False, unigram_probabilities=UNIGRAMS):
	'''Gets a random word from unigrams based on probability.'''
	if unweighted:
		return random.choice(unigram_probabilities[0])
	else:
		while True: # get a new word until you dont have a bad_word
			word = numpy.random.choice(unigram_probabilities[0], p=unigram_probabilities[1])
			if text.check_word(word): # word is ok
				break
			print('bad unigram: {}'.format(word))
		return word


