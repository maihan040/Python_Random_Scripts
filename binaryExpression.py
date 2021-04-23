# binaryExpression.py
# 
# purpose: to evaluate an arithmetic expression as given by a binary tree
# 
# Example: 
#							 * 
#							
#						      /     \
#
#						   +	      +
#
#					 	/     \     /     \
#
#					       3        2  4        5
#
#
# equals: [(3 + 2) * (4 + 5)]

#class definition
class bstNode:
	def __init__(self, d):
		self.left = None 
		self.d = d
		self.right = None

#function definition
def evalExp(node):

	#base cases
	if(node == None):
		return 0

	#return operand
	if(node.left == None and node.right == None):
		return node.d

	#compute the left side of the tree
	left = evalExp(node.left)

	#compute the right side of the tree
	right = evalExp(node.right)

	#determine the operator 
	if(node.d == "+"):
		return left + right

	if(node.d == "-"):
		return left - right

	if(node.d == "*"):
		return left * right

	if(node.d == "/"):
		return left / right


#main 
node = bstNode('*')

#left side
node.left = bstNode('+')
node.left.left = bstNode(3)
node.left.right = bstNode(2)


#right side
node.right = bstNode('+')
node.right.right = bstNode(5)
node.right.left = bstNode(4)

print("The expression = " + str(evalExp(node)))

