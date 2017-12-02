import sys
import csv

def apriori(records, things, mSupport, mConfidence):
	return [(0,0)], [((1, 1), 1, 1)]
	
data = sys.argv[1]
mSupport = float(sys.argv[2])
mConfidence = float(sys.argv[3])
records = []
things = []
with open(data, newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		records.append(row)
		for thing in row:
			things.append(thing)
newThings, newRules = apriori(records, things, mSupport, mConfidence)
output = open('output.txt', 'w')
output.write("==Frequent itemsets (min_sup=" + str(float(mSupport)*100) + "%)\n")
for thing in newThings:
	output.write("[" + str(thing[0]) + "]" + ", " + str(int(float(thing[1])*100)) + "%\n")
output.write("==High-confidence association rules (min_conf=" + str(float(mConfidence)*100) + "%)\n")
for rule in newRules:
	output.write("[" + str(rule[0][0]) + "]" + " => " + "[" + str(rule[0][1]) + "] (Conf: " + str(float(rule[1])*100) + "%, Supp: " + str(int(float(rule[2])*100)) + "%)\n")
