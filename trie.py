class Trie:
	head = {}
	def add(self,word):
		cur = self.head

		for ch in word:
			if ch not in cur:
				cur[ch] = {}
			cur = cur[ch]
		cur['*'] = True 

	def search(self, word):
		cur = self.head 
		for ch in word:
			if ch not in cur:
				return False 
			cur = cur[ch]
			if '*' in cur:
				return True 

		return False 

dictionary = Trie()
dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search('h'))
print(dictionary.search('hi'))
print(dictionary.search('hello'))


