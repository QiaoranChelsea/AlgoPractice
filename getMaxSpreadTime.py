class TreeNode():
	def __init__(self, val):
		self.val = val 
		self.children = []



def getMaxSpreadTime():
	def getMaxSpreadTimeHelper(node):
		if not node:
			return 0

		res = 0 
		for child in node.children:
			if child not in visited:
				tempSum = getMaxSpreadTimeHelper(child)
				if tempSum > res :
					res = tempSum
				visited.add(res)

		return res + node.val 		



	visited = set()

	root = TreeNode(0)
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4) 
	node5 = TreeNode(5)  
	node6 = TreeNode(6) 	

	root.children = [node1,node2, node3,node4]
	node2.children=[node5,node6]


	return getMaxSpreadTimeHelper(root)


print(getMaxSpreadTime())
