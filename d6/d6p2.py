f = open("test-input.txt", "r")
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

def display(orig):
	for line in orig:
		print(''.join(line))
	print()

def getPosition(arr):
	for row in range(len(arr)):
		for col in range(len(arr[i])):
			if arr[row][col] == '^':
				position = [row, col]
				return position

moves = 0
def walk(lines):
	#position = [37, 65]
	position = [6, 4]
	direction = up
	walked = {}
	while (position[0] < height and position[0] > 0 and position[1] < width and position[1] > 0):
		lines[position[0]][position[1]] = 'X'
		if ( str(position) in walked ):
			if (walked[str(position)][0] == 2 and walked[str(position)][1] == direction):
				return False 
			walked[str(position)][0] += 1
		else:
			walked[str(position)] = [0, direction]
		nextPos = [pos + move for pos, move in zip(position, direction)]
		if (nextPos[0] >= height or nextPos[0] < 0 or nextPos[1] >= width or nextPos[1] < 0):
			break

		if lines[nextPos[0]][nextPos[1]] == '#':
			direction = [direction[1], -direction[0]]
		else:
			position = nextPos
	return lines
orig = walk(lines)
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if orig[i][j] == 'X':
			orig[i][j] = '#'
			if (not walk(orig)):
				moves += 1
			orig[i][j] = 'X'
print(moves)	
