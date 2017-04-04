# random_models.py

# utility for returning two random SongWriter models 

from . import simple_models, artist_based
import random

MODELS = {
	'GoogleUnigramSongWriter': simple_models.GoogleUnigramSongWriter,
	'GoogleBigramSongWriter': simple_models.GoogleBigramSongWriter,
	'ArtistBigramSongWriter': artist_based.ArtistBigramSongWriter,
	'ArtistTrigramSongWriter': artist_based.ArtistTrigramSongWriter,
}

def get_models(artist):
	'Select two random models and return their names with their objects'
	model1_name, model2_name  = random.sample(MODELS.keys(), 2)

	# reroll unigram songwriter 60% of the time because it sucks
	if model1_name == 'GoogleUnigramSongWriter':
		roll = random.randint(1, 10)
		if roll > 4:
			model1_name = random.choice(list(MODELS.keys()))
	if model2_name == 'GoogleUnigramSongWriter':
		roll = random.randint(1, 10)
		if roll > 4:
			model2_name = random.choice(list(MODELS.keys()))

	# initialize models
	model1 = MODELS[model1_name](artist)
	model2 = MODELS[model2_name](artist)

	return [model1_name, model2_name, model1, model2]

