import heapq 
import collections

def rearrangeString(words, k):
	if not words:
		return ""

	wlen = len(words)
	if k > wlen:
		return ""

	wordsCount = {}
	heap = []
	for w in words:
		wordsCount[w] = wordsCount.get(w, 0) + 1 

	for w,c in wordsCount.items():
		heapq.heappush(heap, (-c, w))
	res = ""
    
	while heap:

		count = min(k,wlen) ## wlen can be used to keep track of the remaining unasigned word
		used = []
		for i in range(count):
			if not heap:  ## if we didn't assign the k number then there is no word in heap. that means the min part number can't be accoimplished 
				break

			curCount, curWord = heapq.heappop(heap)
			res = res + curWord
			if -curCount >1:
				used.append((curCount + 1, curWord))
			wlen -= 1 
		for item in used:
			heapq.heappush(heap, item)
	return res 	 


# def rearrangeString2(words, k):
# 	_len = len(words)
# 	words_count = collections.Counter(words)
# 	que = []
# 	heapq.heapify(que)
# 	for w, v in words_count.items():
# 		heapq.heappush(que, (-v, w))
# 	res = ""
# 	while que:
# 		cnt = min(_len, k)
# 		used = []
# 		for i in range(cnt):
# 			if not que:
# 				return ""
# 			v, w = heapq.heappop(que)
# 			res += w
# 			if -v > 1:
# 				used.append((v + 1, w))
# 			_len -= 1
# 		for use in used:
# 			heapq.heappush(que, use)
# 	return res




print(rearrangeString("aaadbbcc",3))








