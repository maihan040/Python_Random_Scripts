#
#module name: linkedlist.py
#
#purpose: class definition for a linked list 
#
#date created: 09/04/2019
#
#version: 1.0
#


#########################################################
#			Import modules			#
#########################################################
import node

#########################################################
#			Class definition		#
#########################################################
class linkedlist:

	#constructor
	def __init__ (self, head=None):
		self.head = head

	#print
	def printList(self):
		current = self 
		while current.next is not None: 
			print(str(current.data) + "->", end="")
			current = current.next
		print(current.data)


	#iterative apprach 
	def mergeListIterative(self, l1, l2):
		#locale names
		current = None
		root = None 

		while(True):
			if(l1 == None):
				nextNode = l2
			elif(l2 == None):
				nextNode = l1
			elif(l1.data < l2.data):
				nextNode = l1
			else:
				nextNode = l2

			#advance the position in the respective linkedlist
			if(nextNode == l1): 
				l1 = l1.next if l1 else None
			if(nextNode == l2):
				l2 = l2.next if l2 else None

			#check if end has been reached
			if(nextNode == None):
				break

			#merge the list 
			if not current: 
				current = nextNode
				root = current 
			else: 
				current.next = nextNode 
			current = nextNode

		#return the root of the merged linked list 
		return root 

	#recuriseve approach 
	def mergeListRecursive(self, l1, l2):
		#base case
		if(l1 == None):
			return l2
		elif(l2 == None):
			return l1
		elif(l1.data < l2.data):
			l1.next = self.mergeListRecursive(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeListRecursive(l1, l2.next)
			return l2

	#add two numbers represented as linked lists 
	#Recursive function 
	def addNum(self, first, second):
		root = None
		prev = None
		temp = None
		carry = 0

		while(first is not None and second is not None):
			fdata = 0 if first is None else first.data
			sdata = 0 if second is None else second.data
			sum = fdata + sdata + carry

			#compute the next carry
			carry = 1 if sum >= 10 else 0
			sum = sum if sum < 10 else sum %10
			print("Sum is : " +str(sum))
			temp = node.node(sum)

			#check wheter the head of this list is empty
			if root is None:
				root = temp
			else:
				prev.next = temp
			prev = temp

			#advance both lists
			if first is not None:
				first = first.next
			if second is not None:
				second = second.next

		#add remaining carry if any
		if carry:
			temp.next = node.node(carry)

		#return the root 
		return root

	#reverse list via an iterative approach
	def reverselistIteratively(self, head): 
		if(head == None):
			return None

		#pointers used to keep track as we traverse the list
		root = None
		prev = head
		current = prev.next
		nxt = head.next.next
		prev.next = None

		#traverse the list 
		while(nxt.next != None):
			current.next = prev
			prev = current
			current = nxt
			nxt = nxt.next

		#point the last two nodes
		current.next = prev
		nxt.next = current
		root = nxt

		#return the new head 
		return root

	#reverse list via a recursive approach 
	def reverseListRecursive(self, curr, prev=None):
		#base case
		if curr == None:
			return None
		if curr.next == None:
			curr.next = prev
			return

		
#########################################
#				Driver					#
#########################################
a = node.node(1)
a.next = node.node(3)
a.next.next = node.node(5)

b = node.node(2)
b.next = node.node(8)
b.next.next = node.node(6)

c = node.node(10)
c.next = node.node(12)
c.next.next = node.node(14)

d = node.node(11)
d.next = node.node(13)
d.next.next = node.node(15)

'''
#iteratirve approach
print("-------------------------------------------------------------")
print("Iterative apprach ")
print("First list " )
a.printList()
print("Second list ") 
b.printList()
print("Merging both lists via iterative approach")
result_iterative = linkedlist().mergeListIterative(a,b)
print("The merged linked list is: ")
result_iterative.printList()

#recursive apprach 
print("-------------------------------------------------------------")
print("Recursive apprach ")
print("First list ")
c.printList()
print("Second list")
d.printList()
print("Merging both lists via recursive approach")
result_recursive = linkedlist().mergeListRecursive(c,d)
print("Merged linked list is: ")
result_recursive.printList()

#add numbers 
print("-------------------------------------------------------------")
print("Adding lists")
print("First list ")
a.printList()
print("Second list")
b.printList()
print("Adding both numbers")
result_sum = linkedlist().addNum(a,b)
print("Added linked list is: ")
result_sum.printList()


#reverse list via an iterative approach 
print("-------------------------------------------------------------")
print("Reversing list iteratively")
print("List before reversal ")
a.printList()
rev_list = linkedlist().reverseListRecursive(a, None)
print("After reversal list is: ")
rev_list.printList()
'''

#recursive apprach 
print("-------------------------------------------------------------")
print("Recursive apprach ")
print("First list ")
c.printList()
print("Second list")
d.printList()
print("Merging both lists via recursive approach")
result_recursive = linkedlist().mergeListRecursive(c,d)
print("Merged linked list is: ")
result_recursive.printList()