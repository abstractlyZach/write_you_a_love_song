from models import artist_based

song_writer = artist_based.ArtistBigramSongWriter('data/ngrams/Taylor_Swift.txt')

for i in range(10):
	print(song_writer._build_line())
