import csv
from collections import defaultdict

counts = 0

with open('data/ngrams/count_2w.txt', 'r') as tsvfile:
	reader = csv.reader(tsvfile, delimiter='\t')
	for line in reader:
		counts += 1

print(counts)
		