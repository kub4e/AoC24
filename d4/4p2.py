
mwidth = 140
mheight = mwidth
res = 0
file = open("input.txt", "r")
char_ar = [list(line.rstrip('\n')) for line in file.readlines()]



for row in range(1, mheight-1):
	for col	in range(1, mwidth-1):
		if (char_ar[row][col] == "A"):
			'''
			up_left = char_ar[row-1][col-1]
			up_right = char_ar[row-1][col+1]
			down_left = char_ar[row+1][col-1]
			down_right = char_ar[row+1][col+1]
			'''
			
			ul_word = char_ar[row-1][col-1] + "A" + char_ar[row+1][col+1]
			ur_word = char_ar[row-1][col+1] + "A" + char_ar[row+1][col-1]

			if ( (ul_word == "MAS" or ul_word[::-1] == "MAS") and (ur_word == "MAS" or ur_word[::-1] == "MAS") ):
				res += 1
print(res)
