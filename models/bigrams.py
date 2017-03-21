# bigrams.py

# pretty much only used for simple_models.py
# I wrote this code too specifically and it's making it hard to design for the 
# 	bigger picture.

import csv
import numpy
from collections import defaultdict
from utils import exceptions, text, constants
import copy

def get_bigram_generator_and_enders(file_name='data/ngrams/count_2w.txt'):
	'''Reads a file of bigrams and their counts and returns
	a dictionary linking the first word to a NextWord object that can return
	a next word based on conditional probability
	'''
	bigram_dictionary = defaultdict(NextWord)
	enders = set()
	with open(file_name, 'r') as tsvfile:
		reader = csv.reader(tsvfile, delimiter='\t')
		for bigram, count in reader:
			count = int(count)
			first_word, second_word = bigram.lower().strip().split(' ')
			# add the second word and the count to the entry for the first word
			bigram_dictionary[first_word].add(second_word, count)
			if second_word == '</S>'.lower():
				enders.add(first_word)
	return dict(bigram_dictionary), enders


class NextWord:
	'''Class that handles finding the next word of a bigram, given a starting word.'''
	def __init__(self):
		self._words = []
		self._counts = []
		self._N = 0

	def add(self, word, count):
		self._words.append(word.strip().lower())
		self._counts.append(count)
		self._N += count

	def get_word(self):
		'''Uses conditional probability to find the next word.'''
		probabilities = self._calculate_probabilities()
		return numpy.random.choice(self._words, p=probabilities)

	def possible_words(self):
		return copy.copy(self._words)

	def _calculate_probabilities(self):
		return [count / self._N for count in self._counts]


BIGRAMS, _ = get_bigram_generator_and_enders()
def get_next_word(word, bigrams=BIGRAMS):
	'''Given a word, finds a likely next word using bigrams.'''
	word = word.strip().lower()
	try:
		counter = 0
		while True:
			to_return = bigrams[word].get_word()
			if text.check_word(to_return):
				break # return the word if it's ok
			if counter >= constants.PROFANITY_RETRY:
				print('could not find a reasonable next word for {}.'.format(word))
				break
			counter += 1
		return to_return
	except KeyError:
		raise exceptions.WordNotFoundError(word)
