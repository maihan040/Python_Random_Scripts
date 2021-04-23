#
#module name: queue.py
#
#purpose: Implement a queue given two stacks only 
#
#date created: 10/06/2019
#
#version: 1.0
#

#################################################################################
#				class definition				#
#################################################################################
class queue: 

	#initializer method 
	def __init__(self):

		#declare member variables
		self.enqueue_stack = []
		self.dequeue_stack = []

	#enqueue method
	def enqueue(self, val): 

		#push the value onto the enqueue stack 
		self.enqueue_stack.append(val)

	#dequeue method
	def dequeue(self):

		#check whether the queue has any data to be dequeued 
		if len(self.enqueue_stack) == 0: 
			print("Nothing to dequeue")
			return 

		#empty the enqueue stack 
		for i in range(0, len(self.enqueue_stack)):
			self.dequeue_stack.append(self.enqueue_stack.pop())

		#declare the return value 
		ret_val = self.dequeue_stack.pop()

		#move everything back to the enqueue stack 
		for i in self.dequeue_stack: 
			self.enqueue_stack.append(self.dequeue_stack.pop())

		#return the dequeued value
		return ret_val 

	#print queue method
	def printEnQeueue(self): 
		#local variable
		qLen = len(self.enqueue_stack)

		#print each value 
		for val in self.enqueue_stack: 
			print(str(val) + ' ', end='')

		#print newline
		print()

	#print queue method
	def printDeQeueue(self): 
		#local variable
		qLen = len(self.dequeue_stack)

		#print each value 
		for val in self.dequeue_stack: 
			print(str(val) + ' ', end='')

		#print newline 
		print()


#############################################################
#						  "Main"							#
#############################################################

#instantiate the queue classe
q = queue()

#add values to the queue 
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

#printt he current stack's contents 
print("Current queue is: ", end='')
q.printEnQeueue()

#dequeue the values 
print(str(q.dequeue()))
print(str(q.dequeue()))