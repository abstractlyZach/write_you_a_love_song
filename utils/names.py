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
	'green', 'blue', 'purple', 'brown', 'pink', 'brave', 'calm', 'chivalrous', 'clumsy', 
	'cold', 'confused', 'cool', 'crazy', 'defiant', 'dirty', 'dusty', 
	'embarrassed', 'encouraging', 
	'energetic', 'enthusiastic', 'evil', 'fast', 'fat', 'fluffy', 'funny', 'fuzzy', 
	'gentle', 'giant', 'grumpy', 'handsome', 'happy', 'itchy', 'jittery', 'little', 
	'lonely', 'magnificent', 'lucky', 'mighty', 'modern', 'mute', 'nice', 'obnoxious', 
	'odd', 'perfect', 'pleasant', 'rare', 'relieved', 'subtle', 'sad', 'salty', 
	'shallow', 'silent', 'silly', 'small', 'steady', 'strange', 'swift', 'thoughtful', 
	'victorious', 'vivacious', 'wasteful', 'weary', 'whispering', 'wide-eyed', 'witty', 
	'wonderful', 'worried', 'zany']
	return random.choice(adjectives)

def random_food():
	foods = ['bread', 'cookie', 'potato', 'baked potato', 'burger', 'pot roast', 
	'hot dog', 'steak', 'fries', 'chicken and waffles', 'waffles', 
	'fried chicken', 'bacon', 'eggs', 'toast', 'sandwich', 'chili dog', 
	'nachos', 'coleslaw', 'corn chowder', 'corn', 'donut', 'granola bar', 
	'fortune cookie', 'salad', 'noodles', 'onion rings', 'broccoli', 'fried rice', 
	'celery', 'tomato', 'taco']
	return random.choice(foods)

def random_first_name():
	names = ['jacob', 'michael', 'josh', 'matt', 'daniel', 'chris', 'andrew', 
	'ethan', 'joseph', 'will', 'bill', 'anthony', 'david', 'alex', 'nick', 
	'ryan', 'tyler', 'james', 'john', 'jonny', 'brandon', 'dylan', 'sam', 'ben', 
	'emily', 'maddie', 'emma', 'olivia', 'hannah', 'abigail', 'isabella', 
	'samantha', 'elizabeth', 'ashley', 'alexis', 'sarah', 'sophia', 'alyssa', 
	'grace', 'taylor', 'brianna', 'lauren', 'chloe', 'natalie', 'kayla', 
	'jessica', 'anna', 'victoria', 'michelle', 'hannah', 'kaitlyn', 'jimmy', 
	'sherry', 'bert']
	return random.choice(names)

def random_profession():
	professions = ['singer', 'rapper', 'dancer', 'bass guitarist', 
	'drummer', 'vocalologist-izer', 'cashier', 'waiter', 'chef', 'boss', 
	'student', 'teacher', 'master', 'sumo wrestler', 'adventurer', 
	'wanderer', 'couch potato', 'dreamer', 'truck driver', 'nurse', 
	'sales representative', 'handyman', 'bouncer', 'gym rat', 'body builder', 
	'carpenter', 'software developer', 'real estate agent', 
	'computer system analyst', 'barber', 'pharmacist', 'friend', 'ninja', 
	'samurai', 'pirate', 'wizard', 'sniper', 'fighter', 'thief', 
	'encourager', 'secret agent', 'superhero', 'monkey trainer', 
	'dog whisperer', 'reality show host', 'teenager', 'warchief', 
	'dark knight', 'swordmaster', 'hero', 'bookworm', 'illusionist', 
	'engineer', 'alchemist', 'puppet master', 'storm chaser', 'professor', 
	'waterslide tester', 'critic', 'ostrich babysitter', 'professional snuggler', 
	'elephant stylist', 'expert', 'mall santa', 'inventor', 'class president', 
	'unicorn tender', 'corgi shepherd', 'team mascot', 'ice cream tester', 
	'balloon animal critic', 'stuntman', 'lovely assistant', 'human cannonball', 
	'lion tamer', 'parkour specialist', 'extreme unicyclist', 'cool kid', 
	'viking', 'ranch dressing expert', 'cat behavior consultant', 
	'penguinologist', 'chief shark officer', 'stand-up comedian', 
	'cloud watcher', 'daydreamer', 'unemployed', 'cafeteria microwave technician',
	'tidecaller', 'sun prophet', 'time traveler', 'shoeshinist', 'musician',
	"o'possum tackler", 'vapire']
	return random.choice(professions)

def random_andy_name():
	'''Andy Dwyer's names (Parks and Rec)'''
	names = ['Burt Macklin, FBI', 'Kip Hackman', 'Andy Radical', 'Tim Buckanowski', 
	'Brother Nature', 'Jonny Karate', 'Jonathan Karate', 'Sgt. Thunderfist, MD', 
	'Eagle One', ]
	return random.choice(names)

def random_key_and_peele_name():
	'''Names from the great Key and Peele'''
	names = ["D'Marcus Williums", 'T.J. Juckson', "T'varisuness King", 
	'Tyroil Smoochie-Wallace', "D'Squarius Green, Jr.", 'Ibrahim Moizoos', 
	'Jackmerius Tacktheritrix', "D'Isiah T. Billings-Clyde", 
	"D'Jasper Probincrux III", 'Leoz Maxwell Jilliumz', 
	'Javaris Jamar Javarison-Lamar', 'Davoin Shower-Handel', 'Hingle McCringleberry', 
	"L'Carpetron Dookmarriot", "J'Dinkalage Morgoone", 'Xmus Jaxon Flaxon-Waxon', 
	'Saggitariutt Jefferspin', "D'Glester Hardunkichud", "Swirvithan L'Goodling-Splatt", 
	'Quatro Quatro', 'Ozamataz Buckshank', 'Beezer Twelve Washingbeard', 
	'Shakiraquan T.G.I.F. Carter', 'X-Wing @Aliciousness', 
	'Sequester Grundelplith M.D.', 'Scoish Velociraptor Maloish', 
	'T.J. A.J. R.J. Backslashinfourth V', 'Eeeee Eeeeeeeee', 'Donkey Teeth', 
	'Torque (Construction Noise) Lewith', 'The Player Formerly Known as Mousecop', 
	'Dan Smith', 'Coznesster Smiff', 'Elipses Corter', 'Nyquillus Dillwad', 
	'Bismo Funyuns', 'Decatholac Mango', 'Mergatroid Skittle', 'Quiznatodd Bidness', 
	"D'Pez Poopsie", 'Quackadilly Blip', 'Goolius Boozler', 'Bisquiteen Trisket', 
	'Blyrone Blashinton', 'Fartrell Cluggins', 'Jammie Jammie-Jammie', 'Fudge', 
	'Equine Ducklings', 'Dahistorius Lamystorius', 'Ewokoniad Sigourneth JuniorStein', 
	'Eqqsnuizitine Buble-Schwinslow', "Huka'lakanaka Hakanakaheekalucka'hukahakafaka", 
	'King Prince Chambermaid', 'Ladennifer Jadaniston', 
	'Ladadadaladadadadada Dala-Dadaladaladalada', 'Firstname Lastname', 
	'Squeeeeeeeeeeps', 'A.A. Ron Balakay', 'Mr. Nostrand', 'Mr. Garvey', 'DeVon',
	'Meegan Andre', 'Liam Neesons', 'Vandaveon Huggins', 'Shaboots Michaels', 
	'T-Ray Tombstone']
	return random.choice(names)

def random_alias():
	alias_functions = [random_andy_name, random_key_and_peele_name]
	alias_function = random.choice(alias_functions)
	return alias_function()

def random_parks_and_rec_title():
	titles = ['Cones of Dunshire', 'Real Estate Mogul', 'Mogul Mogul', 'T-Dazzle', 
	'H2Flow', 'Flame Duck', 'Snoop Laser Snake', '5000 Candles in the Wind', 
	"Lil' Sebastian", "Breakfast Cereal", "'Sserts", "Tray Trays", "Sammies", "Sandoozles",
	"Cool Blasterz", "Chicky Chicky Parm Parm", "Chicky Catch", "Super Water", 
	"Bean Blankies", "Food Rakes", "Glitter Factory", "Awesome Sauce", "Entertainment 720",
	"Jean Ralphio", "J-shot", "Ethel Beavers", "Treat Yoself", "Party Scientist",
	"The Club Marine", "Club a Dub Dub", "Tom's Bistro", "What's Crackin'?",
	"Red Carpet Insole", "No One's Trying to Get with Jugglers", "Bet On All the Horses",
	"DJ Roomba", "Fruit Roll-Up Fax", "Eclipse"]
	return random.choice(titles)

def random_mouserat_name():
	names = ['Mouse Rat', 'Scarecrow Boat', 'Malice in Chains', 'Punch Face Champion', 
	'Flames for Flames', 'The Andy Andy Andys',
	'Crackfinger', 'Department of Homeland Obscurity', 'Puppy Pendulum', 
	'Possum Pendulum', 'Radwagon', 'Jet Black Pope', 
	'Muscle Confusion', 'Fiveskin', 'Threeskin', 
	'Angelsnack', 'Nothing Rhymes With Orange', 'Everything Rhymes With Orange', 
	'Nothing Rhymes with Blorenge', 'Andy Dwyer Experience', 
	'Death of a Scam Artist', 'Teddy Bear Suicide', 
	'Two Doors Down', 'Tackle Shaft', 'Hand Rail Suicide', 
	'Rat Mouse']
	return random.choice(names)


# the office

# secret identiies

# arnold schwarzzengar's roles

# random japanese words, maybe japanesizations of english words