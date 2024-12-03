import re

with open("input.txt", "r") as f:
	x = f.read()
	pattern = re.compile(r'mul\((\d+),(\d+)\)')
	matches = pattern.findall(x)
	res = 0
	for match in matches:
		res += int(match[0])*int(match[1])
	print(res)
