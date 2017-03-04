# exceptions.py

class ArtistNotFoundError(Exception):
	'''Exception that is raised when an artist is not found'''
	def __init__(self, artist):
		message = "ArtistNotFoundError: Could not find artist '{}'."
		super(Exception, self).__init__(message.format(artist))

class WordNotFoundError(Exception):
	'''Exception that is raised when a word is not found'''
	def __init__(self, word):
		message = "WordNotFoundError: Could not find word '{}' in the dictionary."
		super(Exception, self).__init__(message.format(word))
