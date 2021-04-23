#!/usr/bin/python3
'''
	four_sum.py

	Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that a + b + c + d = n.

	created: 09/03/2020

	version: 1.0
'''

########################### Import Modules ######################
from binarySearch import binar_search as bs

######################## Function Definition ####################
def four_sum(numbers, target): 

	#variables 
	end = len(numbers) - 1
	result = []

	#validate the input list 
	if end < 0:
		return []

	#sort the numbers. This will help in determining whether 
	#numbers need to be added or removed to a partial sum 
	#in order to reach to the target sum 
	nums = sorted(numbers)

	#iterate through the newly created list 
	for i in range(end - 3):
		for j in range(i + 1, end - 2):
			e = end 

			#copute a partial sum to determine which missing sum 
			#will yield the desired target sum 
			#
			#idea is to keep i,j, and e fixed, and via binary search
			#determine whether the missing digit lies between j and e
			partial_sum = nums[i] + nums[j] + nums[e]
			diff = target - partial_sum
			idx = bs.binary_search(nums[j+1:e], diff, True)	#pass the True flag since the input is already sorted

			#check the possible index from above
			if idx >= 0:
				result.append([nums[i], nums[j], nums[idx], nums[e]])
			else: 
				continue

	#if this section is reached it means there are no possible matches
	#return an empty list 
	return []