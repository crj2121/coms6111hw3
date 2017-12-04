import sys
import csv

#collect the frequency of each item
itemfreq  = {} #(setCount)
#preserves dictionary order 
order = {} # largeOne
everything = {} #largeSet
import itertools

def apriori(records, things, mSupport, mConfidence):
	#check which items are above mSupport
	selected = []
	current= {}
	trans = 0
	uniqueThings = list(set(things))
	for item in uniqueThings:
		for record in records:
			val = True
			for i in item:
				if i in record:
					record.remove(i)
				else:
					val = False

			if item in record or val:
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
			if float((pair[1])/total) >= mSupport:
				selected.append((pair[0]))
		
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

	for c in range(1,totalTrans +1):
		possible = []
		for pair in order.items():
			combos = []
			combos = itertools.combinations(pair[1],c)
			print('hey')
			print(pair[1])
			for combo in combos:
				possible.append(combo)
		for p in possible:
			newCurrent = []
			newCurrent.append(tuple(p))
		print('hey2')
    	#where there's things change with newCurrent 
		selectedTwo = []
		currentTwo= {}
		uniqueThings = list(set(newCurrent))
		for item in uniqueThings:
			print('hey3')
			for record in records:
				if item in record:
					if item in itemfreq:
						itemfreq[item] += 1
					else:
						itemfreq[item] = 0
					if item in current:
						currentTwo[item] += 1
					else:
						currentTwo[item] = 0
        #finding items that are greater than mSupport
			print('d')
			for pair in current.items():
				total = len(records)
				if float((pair[1])/total) >= mSupport:
					selectedTwo.append((pair[0]))
			print('s')
		print(totalTrans)
		print(c)
		print(selectedTwo)






		

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
