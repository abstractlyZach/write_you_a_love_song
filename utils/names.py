# names.py

# utility module for coming up with song names
import random

def random_animal():
	animals = ['cat', 'dog', 'bird', 'bear', 'wolf', 
	'deer', 'horse', 'tiger', 'lion', 'panda', 'snake', 
	'polar bear', 'cow', 'leopard', 'pig', 'puppy', 'monkey', 
	'ape', 'giraffe', 'shark', 'turtle', 'koala', 'raccoon', 
	'crocodile', 'hippo', 'hedgehog', 'otter', 'reindeer', 
	'rhino', 'octopus', 'lizard', 'coyote', 'llama', 'cheetah', 
	'hamster', 'goat', 'parrot', 'donkey', 'bunny']
	return random.choice(animals)

def random_adjective():
	adjectives = ['addicted', 'agreeable', 'amusing', 'ancient', 'angry', 
	'anxious', 'arrogant', 'average', 'beautiful', 'red', 'orange', 'yellow', 
	'green', 'blue', 'purple', 'brown', 'pink', 'brave', 'calm', 'clumsy', 'cold', 
	'confused', 'cool', 'crazy', 'defiant', 'dirty', 'dusty', 'embarrassed', 'encouraging', 
	'energetic', 'enthusiastic', 'evil', 'fast', 'fat', 'fluffy', 'funny', 'fuzzy', 
	'gentle', 'giant', 'grumpy', 'handsome', 'happy', 'itchy', 'jittery', 'little', 
	'lonely', 'magnificent', 'lucky', 'mighty', 'modern', 'mute', 'nice', 'obnoxious', 
	'odd', 'perfect', 'pleasant', 'rare', 'relieved', 'subtle', 'sad', 'salty', 
	'shallow', 'silent', 'silly', 'small', 'steady', 'strange', 'swift', 'thoughtful', 
	'victorious', 'vivacious', 'wasteful', 'weary', 'whispering', 'wide-eyed', 'witty', 
	'wonderful', 'worried', 'zany']
	return random.choice(adjectives)
