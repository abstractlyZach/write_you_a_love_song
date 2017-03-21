from models import artist_based

song_writer = artist_based.ArtistBigramSongWriter('data/ngrams/Bruno_Mars.txt')
song_writer.new_song().print()
