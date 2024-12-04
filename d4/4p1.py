import re

char_ar = {}
x = ''
res = 0
pattern = r"XMAS"
mwidth = 140
mheight = mwidth 

with open("input.txt", "r") as file:
	x = file.read()
	file.seek(0)
	char_ar = [list(line.rstrip('\n')) for line in file.readlines()]


'''char_ar = [
	[ 'a', 'b', 'c' ],
	[ 'd', 'e', 'f' ],
	[ 'g', 'h', 'i' ]
]'''

res += len(re.findall(pattern, x)) # Horizontal, left to right
res += len(re.findall(pattern, x[::-1])) # Horizontal, right to left

for col in range(mwidth): # Vertical top to bottom
	line = ''
	for row in range(mheight):
		line += char_ar[row][col]
	res += len((re.findall(pattern, line)))

for col in reversed(range(mwidth)): # Vertical bottom to top
	line = ''
	for row in reversed(range(mheight)):
		line += char_ar[row][col]
	res += len((re.findall(pattern, line)))

for start_col in range(mwidth): # Diagonal left to right, across x
	line = ''
	col = start_col
	row = 0
	while ( col < mwidth and row < mheight):
		line += char_ar[row][col]
		col += 1
		row += 1
	res += len((re.findall(pattern, line)))
	res += len((re.findall(pattern, line[::-1])))

for start_row in range(1, mheight): # Diagonal left to right across y axis
	line = ''
	row = start_row
	col = 0
	while ( col < mwidth and row < mheight):
		line += char_ar[row][col]
		col += 1
		row += 1
	res += len((re.findall(pattern, line)))
	res += len((re.findall(pattern, line[::-1])))

for start_col in reversed(range(mwidth+1)): # Diagonal right to left across x
	line = ''
	col = start_col
	row = 0
	while ( col > 0 and row < mheight ):
		line += char_ar[row][col-1]
		col -= 1
		row += 1
	res += len((re.findall(pattern, line)))
	res += len((re.findall(pattern, line[::-1])))

for start_row in range(1, mheight):
	line = ''
	row = start_row
	col = mwidth
	while ( row < mheight and col > 0 ):
		line += char_ar[row][col-1]
		col -= 1
		row += 1
	res += len((re.findall(pattern, line)))
	res += len((re.findall(pattern, line[::-1])))

print(res)
