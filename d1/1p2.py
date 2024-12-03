import re
f = open("input.txt", "r")

x = f.read()
l = re.split(r'[ \n]+', x)
l = l[:-1]
left = []
right = []
for i in range(len(l)):
	if i%2 == 0:
		left.append(l[i])
	else:
		right.append(l[i])

for i in range(len(left)):
	left[i] = int(left[i])
	right[i] = int(right[i])

tot = 0
o = 0
for i in range(len(left)):
	o = 0
	for y in range(len(right)):
		if left[i] == right[y]:
			o += 1
	tot += o*left[i] # I INDETED THIS TOO MUCH AND PUT IT IN THE LOOP LOST TIME
print(tot)
