## aaaabbbbbbc => 4xa6xb1xc
def encodeMultipleChar(input):
	if not input:
		return input

	lastElem = '#'
	count = 0
	res = []
	sub = ''
	for i, item in enumerate(input):
		if lastElem == '#':
			lastElem = item
			count = 1 
		else:
			if lastElem != item:
				sub = str(count) + 'x' + lastElem
				res.append(sub)
				count = 1 
				lastElem = item 
			else:
				count += 1 

	res.append(str(count) + 'x' + lastElem)

	return "".join(res)

# print(encodeMultipleChar("aaaabbbbbb"))

def decodeMultipleChar(input):
	if not input:
		return input 

	count = 0 
	alpha = '#'
	res = []
	for item in input:
		if item == 'x':
			continue 
		elif item.isdigit():
			count = int(item)
		elif item.isalpha():
			alpha = item
			res += [item]*count 

	return "".join(res)

print(decodeMultipleChar( encodeMultipleChar("a")))







