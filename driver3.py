import sys
import csv

#collect the frequency of each item
#itemfreq  = {} #(setCount)
#preserves dictionary order 
order = {} # largeOne
everything = {} #largeSet
import itertools

def msupCheck(records, items, mSupport, itemfreq):
	selected = []
	current= {}
	uniqueThings = list(set(things))
	for item in uniqueThings:
		for record in records:
			#val = True
			#for i in item:
				#if i in record:
					#record.remove(i)
				#else:
				#	val = False

			if item in record: #or val:
				if item in itemfreq:
					itemfreq[item] += 1
				else:
					itemfreq[item] = 0
				if item in current:
					current[item] += 1
				else:
					current[item] = 0
        #finding items that are greater than mSupport
		
		for pair in current.items():
			total = len(records)
			if (float(pair[1]))/total >= mSupport:
				selected.append((pair[0]))

	return selected

def apriori(records, things, mSupport, mConfidence):
	#check which items are above mSupport
	itemfreq  = {}
	trans = 0
	selected = msupCheck(records, things, mSupport, itemfreq)
		
	totalTrans = 0
	for record in records:
		trans += 1
		recLen = len(record)
		totalTrans = recLen
		currItems = []
		i=0
		while i < recLen:
			x=0
			while x < len(selected):
				if record[i] in selected[x]:
					select = record[i]
					currItems.append(select)
				x=x+1
			order[trans] = currItems
			i = i+1

	k = 1
	while(k < totalTrans+ 1):
		subsetList = []
		for key, value in order.items():
			for subset in itertools.combinations(value, k):
				subsetList.append(subset)
		print('h')
		currentLarge = [tuple(row) for row in subsetList]
		current = msupCheck(records,currentLarge,mSupport,itemfreq)
		print(current)
		currentLarge = current
		everything[k] = currentLarge
		k = k + 1

	print(currentLarge)
		






		

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
