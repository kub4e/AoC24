f = open("input.txt", "r")
x = f.readlines()

lines = [[*x[i]] for i in range(len(x))]
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
for i in range(len(lines)):
	lines[i] = lines[i][:-1]
height = len(lines)
width = len(lines[0])

def getPosition(arr):
	for row in range(len(arr)):
		for col in range(len(arr[i])):
			if arr[row][col] == '^':
				position = [row, col]
				return position

position = getPosition(lines)
direction = up
moves = 0
while (position[0] < height and position[0] > 0 and position[1] < width and position[1] > 0):
	lines[position[0]][position[1]] = 'X'
	nextPos = [pos + move for pos, move in zip(position, direction)]
	if (nextPos[0] >= height or nextPos[0] < 0 or nextPos[1] >= width or nextPos[1] < 0):
		break

	if lines[nextPos[0]][nextPos[1]] == '#':
		direction = [direction[1], -direction[0]]
	else:
		position = nextPos

for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] == 'X':
			moves += 1
#for line in lines:
#	print(''.join(line))
print(moves)	
