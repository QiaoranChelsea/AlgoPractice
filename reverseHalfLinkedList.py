import math
class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

def reverseHalfLinkedList(head):
	if not head:
		return head 
	if not head.next:
		return head
	## get total number of node 
	cur = head 
	count = 0 
	while cur != None:
		cur = cur.next
		count += 1 
	## the cur will finally point to the None

	if count == 2:
		return head 

	dummy = left = ListNode(-1)
	dummy.next = head 
	## move to the half point 
	half = math.ceil(count/2) 
	for _ in range(half):
		left = left.next 
	## reverse 
	cur = left.next  
	prev = None 
	nxt = None 
	while cur != None:
		nxt = cur.next 
		cur.next = prev 
		prev = cur 
		cur = nxt
	left.next.next = cur
	left.next = prev

	return dummy.next 

def printLinkedList(head):
	while head != None:
		print(head.val)
		head = head.next 

def main():
	node5 = ListNode(5)
	node4 = ListNode(4,node5)
	node3 = ListNode(3,node4)
	node2 = ListNode(2,node3)
	# node2 = ListNode(2)
	node1 = ListNode(1,node2)

	# printLinkedList(node1)
	head = reverseHalfLinkedList(node1)
	printLinkedList(head)

main()


