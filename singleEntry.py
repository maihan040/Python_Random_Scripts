#
#module name: singleEntry.py
#
#purpose: function to determine a which number has a single in a 
#		  list that has double entires 
#
#note: this function has the same function twice
#	   the second iteration will solve the problem with constant space
#date created: 09/12/2019
#
#version: 1.0
#

#################################################################
#			Function Definitions			#
#################################################################
def findSingleEntry(nums):

	#local variables
	num_dict = {}

	#iterate through the list and create a list for each number
	#indicating how many times that number occured
	for num in nums: 
		if num in num_dict:
			num_dict[num].append(num)
		else:
			num_dict[num] = []
			num_dict[num].append(num)

	#detemrine which list has a single entry and return that key
	for key in num_dict.keys():
		if len(num_dict[key]) == 1:
			return key

	#should this point be reached, it means no single entry was 
	#encountered in the list 
	return False

#following will do the same only in constant memory
def findSingleEntryKMem(nums): 
	#iterate through the list and remove each entry
	#check if another such value is still in the list
	for i in range(0, len(nums)): 
		val = nums[i]
		nums[i] = '-'
		if val not in nums:
			return val
		else:
			nums[i] = val 

	#at this point there is no single entry in the list 
	return false 

#############################################
#					Main					#
#############################################
numbers  = [2, 4, 1, 3, 4, 2, 1, 5, 3]
print("Following numbers are in the list: ")
print(numbers)
#single_num = findSingleEntry(numbers)
single_num = findSingleEntryKMem(numbers)
if single_num:
	print("Single entry: " )
	print(single_num)
else: 
	print("No single entry found")