#
#module name: findKthLargest.py
#
#purpose: Given a list of values, find the Kth largest in the list
#
#date created: 10/05/2019
#
#version: 1.0
#

#################################################################
#			function definition			#
#################################################################
def findKthLargest(nums, k):

	#check whether the list is long enough
	if len(nums) <= 1:
		return nums

	#local variables
	num_dict = {}
	num_count = len(nums)

	for num in nums: 
		if num in num_dict:
			num_dict[num] += 1
		else:
			num_dict[num] = 1

	#sort the keys 
	sorted_num = sorted(num_dict)

	#debug 
	print("sorted numbers: " + str(sorted_num))
	return sorted_num[-k]


#################################################################
#				Main				#
#################################################################

#local variables
numbers = [4, 6, 1, 3, 7, 8, 9, 0, 1]
k = 5

print("Numbers which will be passed are: " + str(numbers))
print("Searching for the " + str(k) + " largest")
val = findKthLargest(numbers, k)
print("The retuned value is: " + str(val))