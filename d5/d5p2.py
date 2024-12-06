f = open("input.txt", "r")
x = f.read()
rules = x.split("\n\n", 1)[0]
pages = x.split("\n\n", 1)[1]

pages = [[int(x) for x in y.split(",") if x] for y in pages.split('\n')][:-1]
rules = [[int(x) for x in y.split("|") if x] for y in rules.split('\n')]

def checkLine(line, rules):
	ordered = True 
	for numToCheck in line:
		for rule in rules:
			if (numToCheck == rule[0]):
				#print(f"{rule}, {numToCheck}")
				if(rule[1] in line and line.index(numToCheck) > line.index(rule[1])):
					ordered = False
	return ordered

def calcResult(pgs, rules):
	res = 0
	for line in pgs:
		print(line)
		res += line[len(line) // 2]
	return res

def swap(line, a, b):
	line[a], line[b] = line[b], line[a]
	return line
	
for line in pages:
	if (checkLine(line, rules)):
		line[:] = [0] * len(line)
	while (not checkLine(line, rules)):
		for numToCheck in line:
			for rule in rules:
				if (numToCheck == rule[0]):
					if(rule[1] in line and line.index(numToCheck) > line.index(rule[1])):
						line = swap(line, line.index(numToCheck), line.index(rule[1]))
					#print(f"{rule}, {numToCheck}")
					#if(rule[1] in line and line.index(numToCheck) > line.index(rule[1])):
print(calcResult(pages, rules))
