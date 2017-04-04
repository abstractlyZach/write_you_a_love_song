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
	adjectives = ['able', 'abundant', 'addicted', 'adorable', 'agreeable', 'alive', 
	'amusing', 'ancient', 'angry', 'anxious', 'arrogant', 'average', 'bad', 'beautiful', 
	'better', 'bewildered', 'big', 'blue', 'brave', 'brief', 'brown', 'calm', 
	'careful', 'chivalrous', 'clean', 'clever', 'clumsy', 'cold', 'confused', 
	'cool', 'crazy', 'dead', 'defeated', 'defiant', 'delightful', 'different', 
	'dirty', 'drab', 'dusty', 'eager', 'early', 'easy', 'elegant', 'embarrassed', 
	'empty', 'encouraging', 'energetic', 'enthusiastic', 'evil', 'faithful', 'famous', 
	'fancy', 'fast', 'fat', 'few', 'fierce', 'first', 'fluffy', 'full', 'funny', 
	'fuzzy', 'gentle', 'giant', 'gifted', 'glamorous', 'good', 'great', 'green', 
	'grumpy', 'handsome', 'happy', 'heavy', 'helpful', 'helpless', 'high', 'important', 
	'inexpensive', 'itchy', 'jealous', 'jittery', 'jolly', 'kind', 'large', 'last', 
	'late', 'lazy', 'light', 'little', 'lively', 'lonely', 'long', 'lucky', 
	'magnificent', 'many', 'mighty', 'modern', 'mushy', 'mute', 'mysterious', 'nervous', 
	'new', 'next', 'nice', 'numerous', 'obedient', 'obnoxious', 'odd', 'old', 
	'old-fashioned', 'orange', 'other', 'own', 'panicky', 'perfect', 'pink', 'plain', 
	'pleasant', 'powerful', 'proud', 'public', 'purple', 'quaint', 'quick', 'rapid', 
	'rare', 'red', 'relieved', 'repulsive', 'rich', 'right', 'sad', 'salty', 'same', 
	'scary', 'shallow', 'short', 'shy', 'silent', 'silly', 'slow', 'small', 'sparkling', 
	'sparse', 'steady', 'strange', 'substantial', 'subtle', 'swift', 'tender', 'thankful', 
	'thoughtful', 'thoughtless', 'ugliest', 'uninterested', 'unsightly', 'uptight', 'vast', 
	'victorious', 'vivacious', 'wasteful', 'weary', 'well-adjusted', 'whispering', 
	'wide-eyed', 'witty', 'wonderful', 'worried', 'wrong', 'yellow', 'young', 'zany', 
	'zealous']
	return random.choice(adjectives)

def random_abstract_noun():
	abstract_nouns = ['ability', 'adoration', 'adventure', 'amazement', 'anger', 
	'anxiety', 'apprehension', 'artistry', 'awe', 'beauty', 'belief', 'bravery', 
	'brilliance', 'brutality', 'calm', 'chaos', 'charity', 'clarity', 'coldness', 
	'comfort', 'communication', 'compassion', 'confidence', 'consideration', 
	'contentment', 'courage', 'crime', 'culture', 'curiosity', 'customer', 'death', 
	'deceit', 'dedication', 'defeat', 'delight', 'democracy', 'despair', 'determination', 
	'dexterity', 'dictatorship', 'disappointment', 'disbelief', 'disquiet', 'disturbance', 
	'dreams', 'ego', 'elegance', 'energy', 'enhancement', 'enthusiasm', 'envy', 'evil', 
	'excitement', 'failure', 'faith', 'faithfulness', 'faithlessness', 'fascination', 
	'favoritism', 'fear', 'forgiveness', 'fragility', 'frailty', 'freedom', 'friendship', 
	'generosity', 'goodness', 'gossip', 'grace', 'graciousness', 'grief', 'happiness', 
	'hate', 'hatred', 'hearsay', 'helpfulness', 'helplessness', 'homelessness', 'honesty', 
	'honor', 'hope', 'humility', 'humor', 'hurt', 'idea', 'idiosyncrasy', 'imagination', 
	'impression', 'improvement', 'infatuation', 'inflation', 'information', 'insanity', 
	'integrity', 'intelligence', 'jealousy', 'joy', 'justice', 'kindness', 'knowledge', 
	'laughter', 'law', 'liberty', 'life', 'loss', 'love', 'loyalty', 'luck', 'luxury', 
	'maturity', 'memory', 'mercy', 'misery', 'motivation', 'movement', 'need', 'omen', 
	'opinion', 'opportunism', 'opportunity', 'pain', 'parenthood', 'patience', 
	'patriotism', 'peace', 'peculiarity', 'perseverance', 'pleasure', 'poverty', 'power', 
	'pride', 'principle', 'reality', 'redemption', 'refreshment', 'relaxation', 'relief', 
	'riches', 'romance', 'rumor', 'sadness', 'sanity', 'satisfaction', 'self-control', 
	'sensitivity', 'service', 'service', 'shock', 'silliness', 'skill', 'slavery', 
	'sleep', 'sophistication', 'sorrow', 'sparkle', 'speculation', 'speed', 'strength', 
	'strictness', 'stupidity', 'submission', 'success', 'surprise', 'sympathy', 'talent', 
	'thought', 'thrill', 'tiredness', 'tolerance', 'trust', 'truth', 'uncertainty', 
	'unemployment', 'unreality', 'victory', 'wariness', 'warmth', 'weakness', 'wealth', 
	'weariness', 'wisdom', 'wit', 'worry']
	return random.choice(abstract_nouns)


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

def random_r_bandname():
	'''Band names from /r/bandnames'''
	names = ['Adolf Hipster & The Vinyl Solutions', 'Icing', 'Fleetwood PC', 
	'U. Wot and the M8s', 'TH_ ("Thunderscore")', 'DIS* ("Disaster Risk")', 
	'Too Funk to Drunction', 'Pony Slaystation', 'Ünnëcëssärÿ Ümläüts', 
	'Johnny Narcissist and the Other Guys', 'Blue Eyes White Privilege', 
	'The Stutters and and and and', 'Super Callous Nihilistic Edgy Hipster Posers', 
	'Rad Bromance', 'Bandy McBandface', 'Lettuce, Turnip, The Beet', 
	'Teens of the Phone Age', 'The Perfect Strawberry', 'Four-Dollar Falafel', 
	'The Upside-Down Question Marks', 'The Global Saboteurs', 'The Ergonomic Rebel', 
	'Six-Legged Egyptians', 'Bag of Broccoli', 'Erroneus Concatenation', 
	'The Ping Pong Precedent', 'Festive Party Burka', 'Intermittent at Best', 
	'Backseat Bandits', 'Midnight Tourettes', 'Vegan Gravy', 'Worst-Case Ontario', 
	'Señor Rita', '/-&$ ("Slashdash and Cash")', 
	"Captain Tinnitus & the ᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉᵉ's", 'Al Gore Rhythm ("Algorithm")', 
	'DumbleCore (Harry Potter Metal)', "I'm Very Angry It's Not Butter", 
	'Hispanic at the Disco', 'Guantanamo Bae', 'Politically Correct Pete & the Retards', 
	"That First Bite of Burrito Where There's No Meat and It's Just Tortilla and Sour Cream", 
	'Nasty Woman', 'Bad Hombres', 'Chinese Steel', 'Bigly', 'Tremendous Machine', 
	'Oh God, Not These Guys', "M'tallica", 
	'No. (Yes cover band that actually never plays Yes songs)', 'Petty Theft', 
	"The Promised Band (Jewish Rock 'n Roll)", 'Mage Against the Regime', 
	'Quran Quran (Muslim fans of Duran Duran)', 'Amish Tech Support', 
	'Get Rich or Try Dying', '4 out of 5 Dentists', 'Cliffhanger and the', 
	'Saran the Rapper', 
	'Gavrilo Princip (A Franz Ferdinand Cover Band that Absolutely Kills It)', 
	"The Little Engine Who Literally Can't Even", 'UnawareWolves', 
	"Reckless at Tiffany's", 'Mid-Life ISIS', 'Test Band Please Ignore', 
	'Hot Singles in Your Area', 'AC⚡️DECENT', 'Ctrl-C', 
	'Fantastic Beats and Where to Find Them', "Osama Bin Rockin' and the Taliband", 
	'Mazeltov Cocktail', 'Nasty Woman and the Bad Hombres', 'Didgeridoom', 
	'1024MB (A 1-gig Band)', 'A Flock of Smeagols', 'pot8o pot@o', 'Deathamphetamine', 
	'Plastic Smiles and the Yes-Men', 'Infidel Castro', 'W.E.B. and Da Bois', 
	'Irritable Vowel Syndrome', 'Homeschool Dropouts', 
	"For the last time I'm not picking a name for your stupid band", 'Stairway to Kevin', 
	'The Suavacados', 'The Mex Pistols (Sex Pistols mariachi cover band)', 
	'Donald Funk and the Muslim Band', 'Dwayne and the Hard Rock Johnsons', 
	'Furious George', 'Pastor of Muppets', 'Net Brutality', 
	'Racist Bassist and the One-Man Klan', 'N-Word Scissorhands', 'Back Stabbath', 
	'Wu-Twang Clan (bluegrass Wu-Tang cover band)', 'Banned Name', 
	'Participation Trophy Wife', 'LGBT-Rex', "Phil 'n the Blanks", 
	'Friends with Medical Benefits', 'International Bass Station', 
	'First Degree Sideburns', "Jehovah's Witness Protection", 
	'National Association of Stolen Acronyms', 'We Stole These Instruments', 
	"Homie O'Stasis (Irish biology-rapper)", 'DeadLochs (Scottish death-metal)', 
	'Witty Pop Culture Reference and the Terrible Puns', 'Technoslovakia', 
	'The Catcher in the Rhymes feat D.J. Salinger', 'Nazi Synthesizer', 
	'Hobos with GoPros', "Don't Techno for an Answer", 'Julius Seizure', 
	'Our Drummer is a Cat', 'Rage in Favor of the Machine', 
	'Minivan Halen (suburban mother Van Halen cover band)', 
	'Gratuitous Sax and the Senseless Violins', 
	'Pangaea (might break up in 300 million years)', 'Σ¬∀ ("Sum but not All")', 
	'The Whom', 'We Can Be Gyros', 'Tom Cruise Control', 
	'[a pun on the name of an existing artist or an otherwise common phrase]', 
	'Panic! At Nabisco', 'Alcoholics Unanimous', 'Blamethrower', 'Terminally Chill', 
	'Bob Ross and the Happy Accidents', 'LinkedIn Park', 'Spaghettisburg Address', 
	'Cool Story and the Bros', "You've Probably Never Heard of Them", 
	'Lord Kelvin and the Absolute Zeros', 'Finnish Hymn!', "Cthulhu's Loofah", 
	'Drag (a downtempo Rush cover band)', 'Anything But Rap or Country', 'Qatar Hero', 
	'The Fault in our Tsars', 'Confirmed: They Are Giants', 
	'Our Record Label Told Us Our Bandname Was Too Long So We Fired Them', 'LL Cool Beans', 
	'Underage Thinking', 'Brainfart and the... uhh...', 'Bloodbath and Beyond', 
	'Voice of Treason', 'Harmonica Lewinsky', 'Lucid Screaming', 
	'Existential Dreads (emo reggae)', "How Can Music Be Real If This Band Isn't Real", 
	'The Plain White Teenagers', 'The Right to Remain Violent', 
	'Band Names Do Not HAVE to be Puns', "Oedipus and the Mama's Boys", 'Placebo Overdose', 
	'Macklemost', 'Ellen Degenerate', 'The Seven Deadly Synths', 'Ibuprofanity', 
	'asdfjkl; ("The Home Keys")', 'Gnarly Rae Jepsen', "Broke 'n Hip", 
	'Pro Bono (U2 cover band that only plays free concerts)', 'Ice Cream Socialists', 
	'Sand (a post-rock band)', 'Verday (Spanish Green Day cover band)', 'Quantum Tarantino', 
	'Dodged a Mullet', "Theiy're", '32nds to Mars', 'Abraham LinkedIn', "Murphy's Lawyers", 
	'Police Navidad', 'Death Frets', 'Our Doomed Protagonists', 'Süpërflüöüs Ümläüts', 
	'Haphazard Habanero', 'Accidental Pirate', 'Chick Norris', 'Handheld Hurricane', 
	'Hawhooooo *wind sound*', 'Fortnightly', 'With an I', 'Vaguely Purple', 
	'Diz is not a Phaze', 'Würm', 'Higher Dimensional Sphere', 'Ogre Toddler', 
	'Reluctant Rockstar', 'Too Much Ink', 'Catastrophism', 'Concerned Ninja', 
	'Seismic Vibrations', 'Human Shotput', 'Dumby', 'Shameless Steel', 
	"Why Didn't We Think of That", 'Mushroom Cloud of Mushiness', 'Eternal Sleepover', 
	'Imitation Crab', 'Tasteful Polka Dots', 'Partial Adult', 'Obliviant', 'Celine Dijon', 
	'Collateral Jammage', 'Requiem for a Meme', 
	'Cereal Killer and the Registered Chex Offenders', 'Soviet Reunion', 'TianAnMen^2', 
	'Def Leprosy', 'Friends with Benadryl', 'Ouizer (French Weezer cover band)', 
	'Judge, Judy, Executioner', 'Consensual Saxophone', 'Childish Zamboni', 
	'Horton Hears the Who', 'The Harshmellows', 'We Still Need a Drummer', 
	'Anne Frankenstein', "It's Always Sunni in Babylonia", 'Ramen Numerals', 
	"My Friend's Dumb New Band", 'Band from Club Penguin', 
	'Alien vs Predator vs Brown vs the Board of Education', 
	'Jerry Mandering and the Districts', 'Rachel Slurs', 'Ctrl + Alt + Defeat', 
	'Seven Billion Hostages', 'Clu] ("Club Racket")', 
	'There. We Named the Band After You. Are You Happy, Larry?', 'Red Lobster Cult', 
	'A.C.R.O.N.Y.M.', 'Projectile Dysfunction', 'The Kids Your Parents Warned You About', 
	'Rage Against the Vending Machine', 'Rodeohead (Radiohead country cover band)', 
	'Random Axe of Kindness', 'The Diabeatles', 'Arnie and the Redundants feat. Arnie', 
	'Pho Fighters (Vietnamese Foo Fighters cover band)', 'Food Fighters', 'Woahzone Layer', 
	'SlaughterMelon', 'Breakfast Epiphanies', 'Vigilanticrhist', 'We Forgot Steve', 
	'Balsamic Cigarette', 'Strangers in a Strange Band', 'Disatronauts', 'Mmmmkay Ultra', 
	'The Ampers&s', 'Guitarded', 'Moist Owlets', 
	r'\\\\\\\\\\ ("The Quadruple-Escaped Backslashes")', 
	'Neighborhood Watch Association (N.W.A)', 'Midget Shortage', 
	'Πρ Maniacs ("Pi Rho Maniacs")', 'Terrorhythm', ',KahZ ("Kamikaze")', 
	'Proximity to Ducks', 'The Land Before Rhyme', 'Receding Airlines', 
	'The War on Uggs', 'Ed, Edd, and Edgy', 'Pro-teen Sheikhs', 'Battery and Assault Rifle', 
	'OK Google', 'Obesity (heavy death metal)', 'Hot Fudge Monday', 
	'Aussie Osborne (Australian Black Sabbath cover band)', 'Civil Discobedience', 
	'Hit Singles in Your Area', 'Wayne Jetski', '#cake ("Poundcake")', "Sandra's Bollocks", 
	'Dan Druff and the Itchy Scalps', 'Typo Negatiev', 'We Might Be Midgets', 
	'Apocalypse Later', 'Band, James Band', 'President Evil', 'Thermodynamic Judo', 
	'lol ("man overboard")', 'Neil Patrick Harrison Ford Expedition', 
	'Hoover and the Great Depression (emo)', 'Anaphylactic Rock', 
	'The Bowling Green Massacre', "Manifest Destiny's Child", 'Burgundy 6', 'Robert', 
	'B&', "No, that's really the band name.", 'Fedora Borealis', 'Paper Machete', 
	'The Fibonacci Sequins', 'Drunk Drivers Against Mothers', 'Dope Francis III', 
	'R&B2D2 (soulful Star Wars tribute band)', 'Panic at the Drive-In', '.ıIlIı.', 
	"The Misused Apostrophe's", 'Gif', 'Kawaii Five-O', 'Worst Bass Scenario', 
	'Th Cnsnnts', 'Maro Yolo', 'Marco Yolo', 'Rhymes Against Humanity', 'SOH CAH TOA', 
	'We Are Required by Law to Inform You We Are a Band', 'Savage Patch Kids', 
	'The Soviet Onion', 'The Grooveyard', 'Tron Javolta', 'Go Ask Your Mother', 
	'Lame Impala', 'Intensity in Tent City', 'We Quit Our Day Jobs For This', 
	'Basses Loaded (all-bassist band)', 'Harry Potter and the Copyright Infringers', 
	'The Freudian Slippers', 'Emotherapy', '2th ("Tooth")', 'The Cool Tux Clan', 
	'Doomerang', 'hijklmno ("H2O")', 'Illegally Blind', 
	'The 800-588-2300 Empire Strikes Back', 'Ambeyoncé', 'Brick and Martyr', 
	'Kenny Logout', 'The Holy Ramen Empire', "The and the And's", '2, 4, Sikhs, 8', 
	'Next Time on Dragon Ball Z', 'Susan, Be Anthony', 'Question Marx', 'Shaolin Funk', 
	'Forgetmenauts', 'Routine Poutine', 'Run DMCA', 'Anime of my Enemy', 'Sarcastronauts', 
	'MAYONNOISE', "New World Hors d'oeuvre", 'Ronald Pagan', 'First Name Bassist', 
	'Bards Against Humanity', 'Random Access Melodies', 'The Why Axis', 
	'Stairway to Eleven', 'Party McFly', 'Chords Against Humanity', 
	'Bob Ross Death Squad', 'One Nation Underdog', 'Google It', 'Baroque Obama', 
	'Crystal Methodist', 'Jesus and the Twelve Decibels', 'Vladimir Gluten', 
	'Slow-Mo Sapiens', 'Vincent Van and the Gogh-Goghs', 'Bass Windu', '&wich', 
	'Notorious G.E.D.', 'OCDC', 'Hypewriter', 'Mildly Cyrus', 'Bros and Cons', 
	'Mispeled', 'Common Sensei', 'Flu Fighters', 'The War on Rugs', 'Apocalypse Mao', 
	'S- ("Siphon")', 'Hogwarts Dropouts', 'Fear Itself', 'Habitat for Inhumanity']
	return random.choice(names)



# the office

# secret identiies

# arnold schwarzzengar's roles

# random japanese words, maybe japanesizations of english words