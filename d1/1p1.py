import re
f = open("input.txt", "r")

x = f.read()
l = re.split(r'[ \n]+', x)
left = []
right = []

for i in range(len(l)):
	if i % 2 == 0:
		left.append(l[i])
	else:
		right.append(l[i])

left = left[:-1]

for i in range(len(left)):
	left[i] = int(left[i])
	right[i] = int(right[i])

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
	sum += abs(int(left[i]) - int(right[i]))
print(sum)
	
