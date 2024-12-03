def main(lst):

	row = lst

	safes = 0
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
		return True



def is_ascending(lst):
    return lst == sorted(lst)

def is_descending(lst):
    return lst == sorted(lst, reverse=True)
with open("input.txt", "r") as f:
	x = f.readlines()

	s = [list(map(int, line.split())) for line in x]

	safes = 0
	for row in s:
		if (main(row)):
			safes += 1
		else:
			for i in range(len(row)):
				tmp = row[:i] + row[i + 1:]
				if (main(tmp)):
					safes += 1
					break
	print(safes)


