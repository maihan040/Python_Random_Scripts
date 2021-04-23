#
#module name: checkList.py
#
#purpose: given a list determine whether a single entry can be modified 
#		  such that the list will be non decreasing
#
#date created: 09/13/2019
#
#version: 1.0
#

#################################################
#		Function Definitions		#
#################################################
def checkList(list): 
	#local variables
	modifiable_count = 0

	#check each value in the list with its adjacent entry
	#note if the entry can be adjuseted 
	for i in range(0, len(list) -1):
		if(list[i] > list[i+1]):
			modifiable_count += 1
			if(modifiable_count > 1):
				return False
		else:
			continue

	#once this point has been reached the the list can 
	#be modified such it it will be non decreasing
	return True

#################################################
#			Main			#
#################################################
my_list1 = [13, 4, 7]
my_list2 = [5, 3, 2, 1, 5]

#process the first list 
print("First list is: " + str(my_list1))
modifiable = checkList(my_list1)
if(modifiable):
	print("The list can be modified")
else:
	print("The list is non-modifiable")

#process the seocnd list 
print("Second list is: " + str(my_list2))
modifiable = checkList(my_list2)
if(modifiable):
	print("The list can be modified")
else:
	print("The list is non-modifiable")