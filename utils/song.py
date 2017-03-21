# song.py

class Song:
	def __init__(self, title, artist, verses):
		self._title = title
		self._artist = artist
		self._verses = verses

	def get_title(self):
		return self._title

	def get_artist(self):
		return self._artist

	def get_verses(self):
		return self._verses

	def print(self):
		print('Title: {}'.format(self._title))
		print('Artist: {}'.format(self._artist))
		print()
		for verse in self._verses:
			for line in verse:
				print(line)
			print()
		print()
		print()

	def get_html(self, title=False, artist=False):
		to_return = ''
		if title:
			to_return += '<h1>Title: {}</h1>'.format(self._title)
		if artist:
			to_return += '<h3>Artist: {}</h3>'.format(self._artist)
		for verse in self._verses:
			for line in verse:
				to_return += '<br>' + line
			to_return += '<br>'
		to_return += '<br><br>'
		return to_return