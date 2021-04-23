#
#module name: smallestMissingNum.py
#
#purpose: given a list of random numbers, find the smallest missing positve number 
#
#date created: 10/16/2019
#
#version: 1.0
#

#################################################################################
#				import libraries				#
#################################################################################
from sys import maxsize 

#################################################################################
#				function definition				#
#################################################################################
def findSmallestMissingNum(arr): 

	#validate array length
	if(len(arr) <= 1):
		return -1 

	#local variables
	min_val = maxsize
	max_val = 0
	all_neg = 1

	#iterate through the array
	for i in arr:
		if(i > 0 and i > max_val): 
			max_val = i 
		if(i > 0 and i < min_val): 
			min_val = i 

	#check whether the array only had negative numbers
	if(min_val < maxsize and max_val > 0):\
		all_neg = 0 

	#compute the difference between the min_Val and max_val
	#this will determine the range where the missing value
	#will fall in 
	if not all_neg:
		diff = max_val - min_val
	else:
		return 1 # since all value in the array were all negative, the next positive value would be "1"

	#determine the missing positive value
	for i in range(1, diff):
		if i not in arr: 
			return i

	#all possible positive number in range from min to max are in the array
	return max_val + 1

#############################################################
#						  "Main"							#
#############################################################

#local variables
nums = [3, 4, -1, 1]

returned_val = findSmallestMissingNum(nums)
print("Contents of the array are: " + str(nums))
print("The missing values is: " + str(returned_val))