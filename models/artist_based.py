# artist_based.py

# module for models that create their songs purely based on 
#    artist's original lyrics

from . import basic_songwriter
from . import unigrams, bigrams
from collections import defaultdict
from utils import exceptions, constants, text, song
import csv
import random

class ArtistBigramSongWriter(basic_songwriter.BasicSongWriter):
	def __init__(self, bigram_file_name):
		# self._bigram_counts = dict()
		self._trouble_words = defaultdict(int)
		self._enders = set()
		self._next_word_generator = defaultdict(bigrams.NextWord)
		with open(bigram_file_name, 'r') as tsvfile:
			reader = csv.reader(tsvfile, delimiter='\t')
			for bigram, count in reader:
				count = int(count)
				first_word, second_word = bigram.lower().strip().split(' ')
				# track words that end lines
				if second_word == '</S>'.lower():
					self._enders.add(first_word)
				else: # don't add enders to the generator
					# add the second word and the count to the entry for the first word
					self._next_word_generator[first_word].add(second_word, count)
				# count the number of times each bigram has been seen
				# self._bigram_counts[(first_word, second_word)] = count
		# convert to a regular dict so you can get KeyErrors
		self._next_word_generator = dict(self._next_word_generator)

	def new_song(self):
		road_map = ['verse', 'chorus', 'verse', 'chorus', 'bridge', 'chorus']
		verses = []
		# save a chorus for repetition
		chorus = self._build_verse()
		for section in road_map:
			if section == 'chorus':
				verse = chorus
			else:
				verse = self._build_verse()
			verses.append(verse)
		return song.Song('idk', 'Zach', verses)

	def _build_verse(self, lines=4):
		verse = []
		for line_index in range(lines):
			line_length = random.randrange(5, 12)
			verse.append(self._build_line(length=line_length))
		return verse

	def _build_line(self, length=10):
		previous_word = '<S>'
		string_sequence = []
		while len(string_sequence) < length:
			try:
				need_ender = len(string_sequence) == length - 1
				new_word = self._get_next_word(previous_word, need_ender=need_ender)
			except exceptions.WordNotFoundError:
				print('inserting unigram because of {}'.format(previous_word))
				new_word = unigrams.get_word()
			except exceptions.NoEnderFoundException:
				print("Can't find an ender that follows '{}'. backtracking...".format(previous_word))
				problem_word = string_sequence.pop() # remove problem word
				if self._trouble_words[problem_word] >= constants.NO_ENDERS_RETRY:
					# remove this problem word for leading to another problem word
					string_sequence.pop()
					previous_word = string_sequence[-1]
				else:
					self._trouble_words[problem_word] += 1
					previous_word = string_sequence[-1]
				continue # jump back to top of loop
			string_sequence.append(new_word)             
			previous_word = new_word
		return text.detokenize(string_sequence)
				
	def _get_next_word(self, word, need_ender=False):
		'Given a word, uses conditional probability to find a next word'
		word = word.strip().lower()
		try:
			counter = 0
			while True:
				if need_ender:
					for possible_ender in self._next_word_generator[word].possible_words():
						if possible_ender in self._enders:
							return possible_ender 
					raise exceptions.NoEnderFoundException()
				to_return = self._next_word_generator[word].get_word()
				if text.check_word(to_return):
					break # return the word if it's ok
				if counter >= constants.PROFANITY_RETRY:
					print('could not find a reasonable next word for {}.'.format(word))
					break
				counter += 1
			return to_return
		except KeyError:
			raise exceptions.WordNotFoundError(word)