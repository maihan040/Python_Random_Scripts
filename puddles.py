#
#module name: puddles.py
#
#purpose: given an array of non-negative intergers representing the elevation at each location. Return the amount of water that would accumulate if it rains. 
#
#date created: 10/16/2019
#
#version: 1.0
#

#################################################################################
#				function definition				#
#################################################################################
def capacity(arr): 

	#validate the length of the array to determine whether 
	#it makes sense to process further
	if(len(arr) < 3):
		return 0

	#local variables
	capacity = 0
	indices = []
	max_elevation = max(arr)

	#iterate through each elevation level 
	for i in range(1, max_elevation + 1): 
		
		#clear the array containing the indices
		indices.clear()

		#get all indices containing non zero values
		for arr_idx in range(0, len(arr)):
			if arr[arr_idx] != 0:
				indices.append(arr_idx)

		#compute a gap larger than "1" in the indices array
		for elev_idx in range(1, len(indices)):
			if(indices[elev_idx] - indices[elev_idx - 1] > 1):
				capacity += (indices[elev_idx] - indices[elev_idx - 1] - 1)

		#lower the non zero values of array by "1" to process the next elevation level 
		for arr_idx2 in range(0, len(arr)):
			if arr[arr_idx2] != 0:
				arr[arr_idx2] -= 1

	#return the total capacity 
	return capacity

#####################################################
#						Main						#
#####################################################

#local variables
elevation = [1, 0, 2, 0, 3]

print("Inside the main method")
print("The elevations are " + str(elevation))
print("Calling the capacity function")
cap = capacity(elevation)
print("Max capacity that can be held is: " + str(cap))