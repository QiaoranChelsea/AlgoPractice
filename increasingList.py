def increasingList(N):
	def helper(lastElem, subres, index):
		if lastElem >= 5:
			print(subres[:])
			res.append(subres[:])
			return 

		i = 0
		while 2**i + lastElem <= N:
			subres.append(2**i + lastElem)
			helper(2**i + lastElem,subres, i+1) 
			subres.pop()
			i += 1 
	
	res = []
	subres = []

	helper(-1,[],0)

	return res

increasingList(5)