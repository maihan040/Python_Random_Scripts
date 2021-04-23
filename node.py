#
#module name: node.py
#
#purpose: create the node class which will be used in subsequent classes such as linked lists
#
#date created: 09/04/2019
#
#version: 1.0
#


#########################################################
#			Import modules			#
#########################################################
from __future__ import print_function

#########################################################
#			Class definition		#
#########################################################
class node(object): 
	def __init__(self, d):
		self.data = d
		self.next = None 

	def printList(self):
		current = self 
		while current.next is not None: 
			print(str(current.data) + "->", end="")
			current = current.next
		print(current.data)
