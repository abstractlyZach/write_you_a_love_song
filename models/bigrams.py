# bigrams.py

import csv
import numpy
from collections import defaultdict
from utils import exceptions, text, constants

def read_bigrams(file_name='data/ngrams/count_2w.txt'):
	'''Reads a file of bigrams and their counts and returns
	a dictionary linking the first word to a NextWord object that can return
	a next word based on conditional probability
	'''
	bigram_dictionary = defaultdict(NextWord)
	with open(file_name, 'r') as tsvfile:
		reader = csv.reader(tsvfile, delimiter='\t')
		for bigram, count in reader:
			count = int(count)
			first_word, second_word = bigram.lower().split(' ')
			# add the second word and the count to the entry for the first word
			bigram_dictionary[first_word].add(second_word, count)
	return dict(bigram_dictionary)


class NextWord:
	'''Class that handles finding the next word of a bigram, given a starting word.'''
	def __init__(self):
		self._words = []
		self._counts = []
		self._N = 0

	def add(self, word, count):
		self._words.append(word)
		self._counts.append(count)
		self._N += count

	def get_word(self):
		'''Uses conditional probability to find the next word.'''
		probabilities = self._calculate_probabilities()
		return numpy.random.choice(self._words, p=probabilities)

	def _calculate_probabilities(self):
		return [count / self._N for count in self._counts]


BIGRAMS = read_bigrams()
def get_next_word(word):
	'''Given a word, finds a likely next word using bigrams.'''
	word = word.strip().lower()
	try:
		counter = 0
		while True:
			to_return = BIGRAMS[word].get_word()
			if text.check_word(to_return):
				break # return the word if it's ok
			if counter >= constants.PROFANITY_RETRY:
				print('could not find a reasonable next word for {}.'.format(word))
				break
			counter += 1
		return to_return
	except KeyError:
		raise exceptions.WordNotFoundError(word)
