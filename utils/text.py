# text.py

from . import get_data
from nltk.tokenize.moses import MosesDetokenizer

BAD_WORDS = get_data.get_bad_words()
def check_word(word):
	'''Returns true if the word is OK to use.'''
	return word not in BAD_WORDS

detokenizer = MosesDetokenizer()
def detokenize(words):
	remove_words = []
	# Moses detokenizer can't handle "can't" and "doesn't", so I have to
	for index, word in enumerate(words):
		if word.lower() == "n't":
			remove_words.append(word)
			words[index - 1] = words[index - 1] + word
	for word in remove_words:
		words.remove(word)
	# capitalize first word and all words that are "I"
	words[0] = words[0].capitalize()
	for index, word in enumerate(words):
		if word == "i":
			words[index] = "I"
	return ' '.join(detokenizer.detokenize(words))