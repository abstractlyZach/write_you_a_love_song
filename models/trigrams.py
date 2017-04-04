# trigrams.py

import numpy
from collections import defaultdict
import copy

class NextWord:
	'''Class that handles finding the next word of a trigram, given two starting words.'''
	def __init__(self):
		# maps the next word to how many counts it has
		self._next_tokens = defaultdict(int)
		# boolean that tracks whether or not n has been updated
		self._n_updated = False
		self._n = 0

	def add(self, word, count):
		self._next_tokens[word] += count
		self._n_updated = False

	def get_word(self):
		'''Uses conditional probability to find the next word.'''
		if not self._n_updated:
			self._n = sum(self._next_tokens.values())
			self._n_updated = True
		next_tokens = list(self._next_tokens.keys())
		counts = self._next_tokens.values()
		probabilities = self._calculate_probabilities(counts)
		# print(next_tokens)
		# print(probabilities)
		return numpy.random.choice(next_tokens, p=probabilities)

	def possible_words(self):
		return copy.copy(list(self._next_tokens.keys()))

	def _calculate_probabilities(self, counts):
		return [count / self._n for count in counts]