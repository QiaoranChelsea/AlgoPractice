##         1
##        2 3
##		 4 5 

class TreeNode:	
	def __init__(self,val):
		self.val = val 
		self.left, self.right = None, None 


def isCompleteBT(root):
	if not root:
		return True 

	q = [root]
	isNonFullNodeOccurs = False
	count =0

	while q:
		count +=1 
		node = q.pop(0)
		if node.left:
			if isNonFullNodeOccurs:
				return False 
			q.append(node.left)
		else:
			isNonFullNodeOccurs = True 


		if node.right:
			if isNonFullNodeOccurs:

				return False 
			q.append(node.right)
		else:
			isNonFullNodeOccurs = True 

	return True

def main():
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)


	node1.left = node2
	node1.right = node3
	node2.right = node4

	print(isCompdleteBT(node1))

main()




