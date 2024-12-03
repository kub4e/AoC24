import re

with open("input.txt", "r") as f:
	x = f.read()
	pattern = re.compile(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))')
	state = True

	matches = pattern.finditer(x)
	res = 0
	for match in matches:
		if (match.group(4)):
			state = False
			print(match.group(4))

		elif (match.group(3)):
			state = True
			print(match.group(3))

		elif (match.group(1)):
			if (state):
				res += int(match.group(1)) * int(match.group(2))
			print(match.group(1))
		#res += int(match[0])*int(match[1])
	print(res)
