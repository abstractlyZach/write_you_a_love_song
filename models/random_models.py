# random_models.py

# utility for returning two random SongWriter models 

from . import simple_models, artist_based
import random

MODELS = {
	'GoogleNGramsSongWriter': simple_models.GoogleNGramsSongWriter,
	'ArtistBigramSongWriter': artist_based.ArtistBigramSongWriter,
}
NGRAMS_LOCATION = 'data/ngrams/'

def get_models(artist):
	'Select two random models and return their names with their objects'
	model1_name, model2_name  = random.sample(MODELS.keys(), 2)
	# initialize models
	if model1_name == 'GoogleNGramsSongWriter':
		model1 = MODELS[model1_name](artist)
	if model2_name == 'GoogleNGramsSongWriter':
		model2 = MODELS[model2_name](artist)

	if model1_name == 'ArtistBigramSongWriter':
		model1 = MODELS[model1_name](
							NGRAMS_LOCATION + artist.replace(" ", '_') + '.txt', 
							artist)
	if model2_name == 'ArtistBigramSongWriter':
		model2 = MODELS[model2_name](
							NGRAMS_LOCATION + artist.replace(" ", '_') + '.txt', 
							artist)

	return [model1_name, model2_name, model1, model2]

