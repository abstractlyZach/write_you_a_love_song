import scrapy
import logging

class AZLyricsSpider(scrapy.Spider):
	name = "metrolyrics"

	def __init__(self, *args, **kwargs):
		# turn off the messages that echo everything I scrape
		logger = logging.getLogger('scrapy.core.scraper')
		logger.setLevel(logging.INFO) # only log messages that are INFO level and above
		# init as usual
		super().__init__(*args, **kwargs)	

	def start_requests(self):
		urls = [
			# 'http://www.metrolyrics.com/shape-of-you-lyrics-ed-sheeran.html',
			# 'http://www.metrolyrics.com/you-belong-with-me-lyrics-taylor-swift.html',
			# 'http://www.metrolyrics.com/imagine-dragons-lyrics.html',

			# my selection of artists from the top artists page:
			# 		http://www.metrolyrics.com/top-artists.html
			'http://www.metrolyrics.com/shots-lyrics-imagine-dragons.html',
			'http://www.metrolyrics.com/ed-sheeran-lyrics.html',
			'http://www.metrolyrics.com/bruno-mars-lyrics.html',
			'http://www.metrolyrics.com/disney-lyrics.html',
			'http://www.metrolyrics.com/coldplay-lyrics.html',
			'http://www.metrolyrics.com/adele-lyrics.html',
			'http://www.metrolyrics.com/rihanna-lyrics.html',
			'http://www.metrolyrics.com/eminem-lyrics.html',
			'http://www.metrolyrics.com/justin-bieber-lyrics.html',
			'http://www.metrolyrics.com/taylor-swift-lyrics.html',
			'http://www.metrolyrics.com/lady-gaga-lyrics.html',
			'http://www.metrolyrics.com/drake-lyrics.html',
			'http://www.metrolyrics.com/maroon-5-lyrics.html',
			'http://www.metrolyrics.com/katy-perry-lyrics.html',
			'http://www.metrolyrics.com/michael-jackson-lyrics.html',
			'http://www.metrolyrics.com/the-weeknd-lyrics.html',
			'http://www.metrolyrics.com/prince-lyrics.html',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		window_title = response.css("title::text").extract_first()
		if self.is_song_page(window_title):
			verses = []
			title, artist = self.parse_title(window_title)
			body = response.css("body")
			verse_selectors = body.xpath(
				'//*[contains(concat( " ", @class, " " ), concat( " ", "verse", " " ))]'
				)
			for verse_selector in verse_selectors:
				verse = verse_selector.css('p::text').extract()
				verse = self.clean_verse(verse)
				if verse != []:
					verses.append(verse)
			# text = self.clean_lyrics(text)
			yield {
				'artist': artist,
				'title': title,
				'verses': verses,
			}
		elif self.is_artist_page(window_title):
			for song_link in self.get_song_links_from_artist_page(response):
				yield scrapy.Request(song_link, callback=self.parse)

	def parse_title(self, title_text):
		'''Parses the "title" field of the html (the text that appears as the title of 
		browser window) to return the song title and the artist.

		title follows the pattern: 
		"Taylor Swift - You Belong With Me Lyrics | MetroLyrics"

		Returns (song_title, artist)

		If a window's title text is formatted inconsistently, the artist will be named 'fix please'
		and the whole title text will be entered as the song title.
		'''
		title_text = self.strip_title(title_text)
		# split the title up
		split_string = title_text.split(' - ')
		artist = split_string[0]
		remainder = split_string[1:]
		# check for proper title formatting
		if len(remainder) > 1 or not remainder[0].endswith('Lyrics'):
			artist = 'fix please'
			song_title = title_text
		else:
			song_title = remainder[0][:-7]
		return song_title, artist

	def get_song_links_from_artist_page(self, response):
		'''Returns hyperlinks for song lyric pages when given an artist page.'''
		links = []
		selectors = response.xpath(
			'//*[(@id = "popular")]//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]'
			)
		for selector in selectors:
			links.append(selector.css('a::attr("href")').extract_first())
		return links

	def strip_title(self, window_title):
		'''strips the '| metrolyrics' from the title'''
		return window_title.split(' | ')[0]

	# There are 3 types of pages we are concerned with: first_letter, artist, and song
	# 	first_letter title looks like: Search for Music Artists and Song Lyrics n
	# 	artist       title looks like: 2 Chainz Song Lyrics
	#	song         title looks like: Ed Sheeran - Shape Of You Lyrics

	def is_artist_page(self, window_title):
		'''Returns true if the window_title is for an artist's page.
		Artist page links follow this pattern:
		2 Chainz Song Lyrics
		'''
		window_title = self.strip_title(window_title)
		return window_title.endswith('Song Lyrics')

	def is_song_page(self, window_title):
		'''Returns true if the window_title is for a song's page.'''
		window_title = self.strip_title(window_title)
		return ' - ' in window_title

	def is_first_letter_page(self, window_title):
		'''Returns true if the window_title is for a first letter page.'''
		window_title = self.strip_title(window_title)
		return window_title.startswith('Search for Music Artists and Song Lyrics')

	def clean_verse(self, verse):
		'''Cleans a verse so that the text comes out correctly.'''
		cleaned_verse = []
		# Remove bracketed sections
		#   like in http://www.metrolyrics.com/shots-lyrics-imagine-dragons.html
		for line in verse:
			start = line.find('[')
			end = line.find(']')
			while start != -1: # while an opening bracket is found
				if end == -1: # avoid infinite loop if some doofus forgot to close their bracket.
					line = ''
				else:
					line = line[ :start] + line[end+1: ]
				start = line.find('[')
				end = line.find(']')
			if line.strip() != '':
				cleaned_verse.append(line.strip()) # trying with stripping the line. 
												# I don't think this should change anything
		return cleaned_verse



