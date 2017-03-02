import re

text = ["\r\n", "\r\n", "\r\n   ", "\r\n", "\r\n\r\n", "\r\n", "\r\n\r\n", 
"\r\n", "\r\n", "\r\n", "\r\n", "\r\n", "\r\n", "\r\n", "\r\n", "\r\n", "\r\n\r\n", 
"\r\n\r\n", "\r\n", "\r\n", "\r\n\r\n", "\r\n", "\r\n", "\r\n\r\n", "\r\n", "\r\n\r\n", 
"\r\n", "\r\nOn a dark desert highway, cool wind in my hair", 
"\nWarm smell of colitas, rising up through the air", 
"\nUp ahead in the distance, I saw a shimmering light", 
"\nMy head grew heavy and my sight grew dim", "\nI had to stop for the night", 
"\nThere she stood in the doorway;", "\nI heard the mission bell", 
"\nAnd I was thinking to myself,", "\n\"This could be Heaven or this could be Hell\"", 
"\nThen she lit up a candle and she showed me the way", 
"\nThere were voices down the corridor,", "\nI thought I heard them say...", "\n", 
"\nWelcome to the Hotel California", "\nSuch a lovely place (Such a lovely place)", 
"\nSuch a lovely face", "\nPlenty of room at the Hotel California", 
"\nAny time of year (Any time of year)", "\nYou can find it here", "\n", 
"\nHer mind is Tiffany-twisted, she got the Mercedes bends", 
"\nShe got a lot of pretty, pretty boys she calls friends", 
"\nHow they dance in the courtyard, sweet summer sweat.", 
"\nSome dance to remember, some dance to forget", "\n", "\nSo I called up the Captain,", 
"\n\"Please bring me my wine\"", 
"\nHe said, \"We haven't had that spirit here since nineteen sixty nine\"", 
"\nAnd still those voices are calling from far away,", 
"\nWake you up in the middle of the night", "\nJust to hear them say...", "\n", 
"\nWelcome to the Hotel California", "\nSuch a lovely place (Such a lovely place)", 
"\nSuch a lovely face", "\nThey livin' it up at the Hotel California", 
"\nWhat a nice surprise (what a nice surprise)", "\nBring your alibis", "\n", 
"\nMirrors on the ceiling,", "\nThe pink champagne on ice", 
"\nAnd she said \"We are all just prisoners here, of our own device\"", 
"\nAnd in the master's chambers,", "\nThey gathered for the feast", 
"\nThey stab it with their steely knives,", "\nBut they just can't kill the beast", 
"\n", "\nLast thing I remember, I was", "\nRunning for the door", 
"\nI had to find the passage back", "\nTo the place I was before", 
"\n\"Relax, \" said the night man,", "\n\"We are programmed to receive.", 
"\nYou can check-out any time you like,", "\nBut you can never leave! \"\n", 
"\r\n\r\n", "\r\n\r\n", "\r\n", "\r\n", "\r\n\r\n", "\r\n\r\n", "\r\n\r\n", "\r\n", 
"\r\n", "\r\n\r\n", "\r\n\r\n", "\r\n", "Visit www.azlyrics.com for these lyrics.", 
"\r\n", "\r\n\r\n", "\r\n\r\n", "\n", "\r\n\r\n", "\r\n", "\r\n", "\r\n\r\n", "\r\n", 
"\n", "\n", "\r\n\r\n", "\r\n", "\r\n\r\n", "\r\n", "\r\n  ", "\r\n", "\r\n\r\n", "\r\n", 
"\r\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\r\n", "\r\n\r\n", "\r\n  ", 
"\r\n", "\r\n\r\n", "\r\n", "\r\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", 
"\n", "\n", "\n", "\n", "\n", "\n", "\r\n", "\r\n\r\n", "\r\n\r\n        ", "  \r\n\t\t", 
"\r\n       \t\t", "\r\n \t  ", "\r\n\r\n", "\r\n", "\r\n", "\r\n\r\n", " ", "\r\n\r\n", 
"\r\n   ", "\r\n", "\r\n", "\r\n"]

header

# print()
# print("=" * 18 + "BEGIN" + "=" * 18)
# print()

# PARAGRAPH_BREAK = '**paragraph break**'

# footer_index = text.index("Visit www.azlyrics.com for these lyrics.")

# text = text[:footer_index] # strip off the standard page footer and below

# # print("footer index = " + str(footer_index))
# # for index, line in enumerate(text):
# # 	if line == '\n':
# # 		print(text[index - 1])
# # 		print(index)
# # print()

# for index, line in enumerate(text):
# 	if line == '\n':
# 		text[index] = PARAGRAPH_BREAK

# text = [line.strip() for line in text] # remove the carriage returns and newlines

# for index, line in enumerate(text):
# 	if line == PARAGRAPH_BREAK:
# 		text[index] += '\n'

# # remove empty lines (empty because they were just newline characters)
# text = [line for line in text if line != ''] 

# text.append(PARAGRAPH_BREAK) # add paragraph break to final paragraph

# for line in text:
# 	print(line)
# print()