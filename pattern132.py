#!/usr/bin/python3

#
# pattern132.py
#
# Description: given a list of numbers, determine if the pattern "132" can be formed 
#
# Created: 6/01/2020
#
# Developer: codex040
#
# Version: 1.0
#

######################### Function definition ######################### 
def find13(nums):

	#local variables
	length = len(nums)

	#validation check 
	if length <= 3:
		return False

	#more local variables
	mins = []			#list to track all mins seen during iteration. The index of this list will show the 
						#min (index "i") for the correspnding index (index "j") of the "nums" list
	min_i = nums[0]		#keep track of lowest min seen thus far
	patterns = []		#used to keep track of the possible patterns 
	stack = []			#used to keep track of possbile values for index "k"

	#populate the "mins" array 
	for j in range(length):
		min_i = min(min_i, nums[j])
		mins.append(min_i)

	#iterate through the passed "nums" list to see if a combination can be created
	for j in range(length - 1, -1, -1):
		if nums[j] > mins[j]:
			#clear the stack of any values that are smaller than "i"
			while(len(stack) > 0 and stack[-1] <= mins[j]):
				stack.pop()
			#check if we have a pattern that matches
			if(len(stack) > 0 and stack[-1] < nums[j]):
				patterns.append((mins[j], nums[j], stack[-1]))
			else: 
				stack.append(nums[j])

	#check if patterns are found and return 
	if patterns: 
		print(patterns)
		return True
	else:
		return False

######################### Main section of the program ######################### 

#local variables 
numbers = [6, 12, 3, 4, 6, 11, 20]
result = find13(numbers)

#check whether the "numbers" list contains the desired "132" pattern
if result: 
	print("Possible to form a 13 patter")
else: 
	print("Not possible to form a 13 patten")
