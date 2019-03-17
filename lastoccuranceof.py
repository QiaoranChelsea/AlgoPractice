
class MyString:
	def __init__(self, mStr):
		self.mStr = mStr
		self.mLen = len(mStr)

    ## abcab  5
    ## ab    2
	def lastoccurenceof(self,subStr):
		k = len(subStr)
		res = -1 
		for i in range(self.mLen - k+1):
			if self.mStr[i:i+k] == subStr:
				res = i
		return res 

def main():
	s = MyString("abcab")
	ans = s.lastoccurenceof("ab")

	print(ans)
main()