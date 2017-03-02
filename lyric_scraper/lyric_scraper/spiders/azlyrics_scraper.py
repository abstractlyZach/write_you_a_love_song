import scrapy
import logging
import urllib.parse

PARAGRAPH_BREAK = '**paragraph break**\n'

class AZLyricsSpider(scrapy.Spider):
	name = "azlyrics"

	def __init__(self, *args, **kwargs):
		# turn off the messages that echo everything I scrape
		logger = logging.getLogger('scrapy.core.scraper')
		logger.setLevel(logging.INFO) # only log messages that are INFO level and above
		# init as usual
		super().__init__(*args, **kwargs)	

	def start_requests(self):
		urls = [
			# 'http://www.azlyrics.com/lyrics/eagles/hotelcalifornia.html',
			# 'http://www.azlyrics.com/lyrics/moanacast/yourewelcome.html',
			# 'http://www.azlyrics.com/i/imaginedragons.html',
			# 'http://www.azlyrics.com/d/daughter.html', # should get 39 songs
			'http://www.azlyrics.com/t/taylorswift.html',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		if self.is_song_page(response.url):
			window_title = response.css("title::text").extract_first()
			artist, title = self.parse_title(window_title)
			body = response.css("body")
			div = body.xpath("//div")
			text = div[10].css('div::text').extract()
			# print(text)
			text = self.clean_lyrics(text)
			yield {
				'artist': artist,
				'title': title,
				'text': text,
			}
		elif self.is_artist_page(response.url):
			for link in self.get_song_links_from_artist_page(response):
				yield scrapy.Request(link, callback=self.parse)
		else:
			print("unknown page type!")

	# There are 3 types of pages we are concerned with: first_letter, artist, and song
	# 	first_letter links look like: http://www.azlyrics.com/w.html
	# 	artist       links look like: http://www.azlyrics.com/i/imaginedragons.html
	#	song         links look like: http://www.azlyrics.com/lyrics/moanacast/yourewelcome.html

	def is_artist_page(self, url):
		'''Returns true if the url is an artist's page.
		Artist page links follow this pattern:
		http://www.azlyrics.com/i/imaginedragons.html
		'''
		path = urllib.parse.urlparse(url).path
		return path[0] == '/' and path[2] == '/'

	def is_song_page(self, url):
		'''Returns true if the url is a song's page.'''
		path = urllib.parse.urlparse(url).path
		return path[:8] == '/lyrics/'

	def is_first_letter_page(self, url):
		'''Returns true if the url is a first letter page.'''
		# assumes we only have 3 types of pages.
		return not self.is_artist_page(url) and not self.is_song_page(url)

	def get_song_links_from_artist_page(self, response):
		'''Returns hyperlinks for song lyric pages when given an artist page.
		'''
		body = response.css('body')
		album_list = body.css('div[id="listAlbum"]')
		relative_song_links = album_list.css('a[target="_blank"]::attr("href")').extract()
		song_links = [response.urljoin(link) for link in relative_song_links]
		return song_links

	def clean_lyrics(self, lyrics, paragraph_break=PARAGRAPH_BREAK):
		'''Cleans the lyrics text so that all that is left are the verses separated by 
		the paragraph break.
		'''
		# strip off everything below the standard page footer 
		footer_index = lyrics.index("Visit www.azlyrics.com for these lyrics.")
		lyrics = lyrics[:footer_index]

		# add paragraph breaks
		for index, line in enumerate(lyrics):
			if line == '\n':
				# only adds the paragraph break if the \n character isn't placed 
				#    before another \n. Happens when there are italics, like
				#	 http://www.azlyrics.com/lyrics/moanacast/yourewelcome.html
				if not lyrics[index + 1].isspace():
					lyrics[index] = PARAGRAPH_BREAK

		# remove the carriage returns and newlines
		lyrics = [line.strip() for line in lyrics] 

		# re-add newline characters after every paragraph break
		# 	the \n characters make for better printing
		#	and you can search for the paragraph break to parse it out later
		for index, line in enumerate(lyrics):
			if line == PARAGRAPH_BREAK.strip():
				lyrics[index] += '\n'

		# remove empty lines (mostly the ones that were cleared with the strip operation)
		lyrics = [line for line in lyrics if line != ''] 

		# add paragraph break to final paragraph
		lyrics.append(PARAGRAPH_BREAK) 

		return lyrics

	def parse_title(self, title):
		'''Parses the "title" field of the html (the text that appears as the title of 
		browser window) to return the song title and the artist.

		title follows the pattern: 
		"EAGLES LYRICS - Hotel California"
		'''
		return title.split(" LYRICS - ")