import sys
import csv
import itertools
from operator import itemgetter

everything = {} 
itemfreq  = {}
order = {} 

def msupCheck(records, items, mSupport):
	selected = []
	current= {}
	uniqueThings = list(set(items))

	#print(uniqueThings)
	for item in uniqueThings:
		for record in records:
			exam= []
			val = True
			for y in record:
				exam.append(y)
			try:
				for i in item:
					exam.remove(i)
					val = True

			except ValueError:
				val = False
			
			if item in record or val:
				if item in itemfreq:
					itemfreq[item] += 1
				else:
					itemfreq[item] = 1
				if item in current:
					current[item] += 1
				else:
					current[item] = 1
        #finding items that are greater than mSupport
		
		for pair in current.items():
			total = len(records)
			if (float(pair[1]))/total >= mSupport:
				if pair[0] not in selected:
					selected.append((pair[0]))
	return selected

def apriori(records, things, mSupport, mConfidence):
	#check which items are above mSupport
	
	trans = 0
	selected = msupCheck(records, things, mSupport)	
	finalItems  = []
	Rules = []
	totalTrans = 0
	for record in records:
		trans += 1
		recLen = len(record)
		totalTrans = recLen
		currItems = []
		i=0
		while i < recLen:
			x = 0
			while x < len(selected):
				if record[i] in selected[x]:
					select = record[i]
					currItems.append(select)
				x +=1
				order[trans] = currItems
			i +=1

	for i in range(1,totalTrans +1):
		possible = []
		for pair in order.items():
			combos = []
			combos = itertools.combinations(pair[1], i)
			for combo in combos:
				possible.append(combo)
		newCurrent = []
		for p in possible:
			newCurrent.append(tuple(p))
		#currentLarge = [tuple(row) for row in possible]
		newSelect = msupCheck(records,newCurrent,mSupport)
		everything[i] = newSelect

	allRecs = len(records)
	for pair in everything.items():
		i =0
		while i < len(pair[1]):
			#gather final items
			first = list(pair[1][i])
			finalItems.append(first)
			level = float(itemfreq[(pair[1][i])])/allRecs
			finalItems.append(float(level))

			i = i +1 
			#gather final rules support 
	for pair in everything.items():
		i =0
		while i < len(pair[1]):
			elm = pair[1][i]
			gather = itemfreq[elm[0]]/allRecs
			conf = float(level/gather)
			changedList = []
			#removing the first element of elm
			changedList = list(elm[1:])
			
			if changedList:
				if mConfidence <= conf:
					Rules.append(((elm[0], changedList), conf, level))
			i = i +1

	return finalItems, Rules
	
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
it = iter(newThings)
newerThings = zip(it, it)
newestThings = sorted(newerThings, key=lambda x: x[1], reverse = True)
for thing in newestThings:
	output.write(str(thing[0]) + ", " + str(int(float(thing[1])*100)) + "%\n")
output.write("==High-confidence association rules (min_conf=" + str(float(mConfidence)*100) + "%)\n")
for rule in newRules:
	output.write(str(rule[0][0]) + " => " + str(rule[0][1]) + " (Conf: " + str(float(rule[1])*100) + "%, Supp: " + str(int(float(rule[2])*100)) + "%)\n")
