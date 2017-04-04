# from models import artist_based

# song_writer = artist_based.ArtistTrigramSongWriter('Imagine Dragons')
# song = song_writer.new_song()
# song.print()


# from models import random_models
# for i in range(5):
# 	model1, model2, _, _ = random_models.get_models('Bruno Mars')
# 	print( model1 + " || " + model2)

from models import simple_models
song_writer = simple_models.GoogleUnigramSongWriter()
song = song_writer.new_song()
song.print()