# ngrams_cleaner.py

# unzips the .gz files, selects the lines that are wanted, writes to new text files,
#	and then deletes the .gz files

# turns out that the google ngrams data is REALLY BIG.
# the compressed files filled up my 157 GB external hard drive.
# Compressed. And I didn't even finish downloading all of the ngram data.
# Good thing I was able to collect the files that I needed. I removed
# all of the files that started with numbers or POS tags.

import gzip
import os
import sys

# command line input for the target directory
relative_path = sys.argv[1]
absolute_path = os.path.abspath(relative_path)

filenames = os.listdir(absolute_path)
gz_filenames = [filename for filename in filenames if filename.endswith('.gz')]

# check to make sure this is the correct directory
print()
print('Are you sure you want to use this directory?')
print('   {}'.format(absolute_path))
print()
print('5 .gz files from this directory:')
file_counter = 0
for filename in gz_filenames:
	if file_counter < 5:
		print('    ' + filename)
		file_counter += 1
input('<Enter> to continue...')


file_counter = 0
for filename in gz_filenames:
	file_path = os.path.join(absolute_path, filename)
	new_file_path = os.path.join(absolute_path, filename[:-3] + '-cleaned.txt')
	if file_counter < 1:
		file_counter += 1
		# use gzip to read the file instead of the standard open()
		with gzip.open(file_path, 'r') as old_file, \
				open(new_file_path, 'w', encoding = 'utf-8') as new_file:
			prev_line = ''
			for current_line in old_file:
				current_line = current_line.decode('utf-8')
				print(current_line)
				prev_line = line

				# wow, this is a lot of work and computing time. 
				# also, it's killing my disk space!!!
				# using Norvig's processed data for the time-being
