# utils.py

# utilities for the scripts directory

def keep_line(line):
	'''Returns a boolean telling whether or not to keep a line from the ngrams file'''
	to_return = True
	# # remove lines with '_' in them because lines with '_' have POS tags,w 
	# if '_' in line:
	return True