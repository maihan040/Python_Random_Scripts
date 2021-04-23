#
#module name: fourSums.py
#
#purpose: given a list determine whether there are four 
#		  values that can add up to a specified target
#
#date created: 09/13/2019
#
#version: 1.0
#

#################################################################
#			Function Definitions			#
#################################################################
def fourSums(list, target):
	#local variables
	result = []
	solution = []

	##########################################################
	#STILL NEEDS WORK 
	#FIX THIS 

	#iterate through the list and compare four values at a time
	for left in range(0, len(list) - 1):
		#debug
		print("Now working on index : " +str(left))
		left1 = left + 1
		for left1 in (left1, len(list) - 3):
			#debug
			print("Left is : " +str(left1))
			left2 = left + 1
			left3 = left2 + 1

			#print the current numbers which are about to be added
			print("Left : " + str(list[left]))
			print("Left1 : " + str(list[left1]))
			print("Left2 : " + str(list[left2]))
			print("Left3 : " + str(list[left3]))
			current_sum = list[left] + list[left] + list[left2] + list[left3]
			if(current_sum == target):	
				solution.extend([list[left], list[left], list[left2], list[left3]])

		#return the list of lists containing all
		#the possible solutions
		return solution

#############################################
#					Main					#
#############################################
my_list = [1, 0, -1, 0, 1, 2]
target = 0

print("Contents of the list are: " + str(my_list))
print("The target is : " + str(target))
solutions = fourSums(my_list, target)
if(solutions):
	print("The solutions are: " )
	print(solutions)
else: 
	print("No solutions possible")