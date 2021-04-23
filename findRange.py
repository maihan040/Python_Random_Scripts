#!/usr/bin/python3

'''
	find_range.py

	Given a sorted array, with possible duplicated values and a given target, find the first and last index where that target is
	Return -1 if there is no entry in the list 

	created: 09/25/2020

	version: 1.0
'''

################################ function definition ########################################
def bin_search(arr, s_idx, e_idx, target):

	#base case 
	if s_idx == e_idx:
		if arr[s_idx] == target:
			return s_idx
		else: 
			return -1

	#find the midpoint and check whether that's the location of the target value
	mid = (s_idx + e_idx)//2

	if arr[mid] == target: 
		return mid 
	elif arr[mid] > target: 
		return bin_search(arr, s_idx, mid - 1, target)
	else: 
		return bin_search(arr, mid + 1, e_idx, target)


def find_range(arr, target):

	#local variables 
	first = last = bin_search(arr, 0, len(arr) - 1, target)
	e_idx = len(arr)
	


	#check the result and terminate the function if the result is not found 
	if (first == -1):
		return -1

	#traverse to both left and right to find the first and last position 
	#keep close track to ensure it's not going out of bounds 
	prev = first - 1

	while 1: 
		if prev != -1 and arr[prev] == target: 
			first -= 1
			prev -= 1
		else: 
			break

	nxt = last + 1

	while 1: 
		if nxt != e_idx and arr[nxt] == target: 
			last += 1
			nxt += 1
		else:
			break

	#return the range
	return (first, last)

###################################  main function  ##########################################
#local variables 
arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6]

#call the function 
idx = find_range(arr, 4)

#check whether the value was in the array and display the result
if (idx == -1):
	print("Value was not in the array")
else: 
	print("Range is : " +str(idx[0]) + "," +str(idx[1]))
