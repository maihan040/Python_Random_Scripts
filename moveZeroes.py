#
#module name: moveZeros.py
#
#purpose: Given a list of values, move all the zeroes to the end of the list
#
#date created: 10/05/2019
#
#version: 1.0
#

#################################################################################
#				function definition				#
#################################################################################
def moveZeros(values):

	#check whether the list needs to be processed
	if len(values) <= 1:
		return values

	#local variables
	zeroesList = []
	values_count = len(values)
	i = 0

	#iterate through the list and pop any "0" entry
	while i < values_count:
		if values[i] == 0:
			values.pop(i)
			values_count -= 1
			zeroesList.append(0)
		else: 
			i += 1

	#extend the reduced list by the number of zeroes that were removed
	values.extend(zeroesList)

	#return the new list
	return

#################################################################################
#					Main					#
#################################################################################

#local variables
numbers = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]

print("Numbers before the zeroes have been moved: " +str(numbers))
moveZeros(numbers)
print("Numbers after the zeroes have been moved: " +str(numbers))
