def main():
	f = open("input.txt", "r")

	x = f.readlines()

	s = [list(map(int, line.split())) for line in x]

	safes = 0
	for row in s:
		safe = True
		for i in range(len(row)):
			if (i+1 < len(row)):
				if (abs(row[i] - row[i+1]) >= 1 and abs(row[i] - row[i+1]) <= 3):
					continue
				else:
					safe = False
			else:
				continue
		if (safe == True and (is_ascending(row) ^ is_descending(row))):
			safes += 1
	print(safes)

	

def is_ascending(lst):
    return lst == sorted(lst)

def is_descending(lst):
    return lst == sorted(lst, reverse=True)

main()
