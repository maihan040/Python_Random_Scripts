#!/usr/bin/python3
'''
	min_range_to_sort.py

	Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

	Example:
	Input: [1, 7, 9, 5, 7, 8, 10]
	Output: (1, 5)


	created: 08/30/2020

	version: 1.0
'''

################################## Function Definitions ###############################
def find_min_range(numbers):

	#local variables
	n = len(numbers)
    indices = []
	temp = sorted(numbers)

	#validation check
	if n == 0:
		return indices

	#compute the indices where the numbers are not in the correct order
	for i in range(n):
		temp[i] = temp[i] - numbers[i]

	#compute start/end indices of sub ranges that need to be sorted
	#and add them in the "indices" list
    while i < n:
		if temp[i] != 0:

			#note down start index
			start = i

			#find the end index of the current sub range
			while temp[i] != 0:
				i += 1

			#note down end index
			end = i - 1

			#add the tuple to the indices list
			indices.append((start, end))
		else:
			continue

	#return the "indices" list
	return indices

############################### Main Section  ###############################
nums = [1, 7, 9, 5, 7, 8, 10]

print("Current list : " + str(nums))
indices = find_min_range(nums)

print("Sub range of elements that need to be sorted: " )
for pair in indices:
	print(str(pair))