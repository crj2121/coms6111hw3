import sys
import csv

data = sys.argv[1]
minSupp = float(sys.argv[2])
minConf = float(sys.argv[3])
with open(data, newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		for thing in row:
			print(thing)
