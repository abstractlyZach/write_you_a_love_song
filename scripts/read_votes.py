import csv
from collections import defaultdict

votes = defaultdict(int)
with open('votes.txt', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for winner, loser, artist in reader:
		votes[winner] += 1

print(votes)
		
