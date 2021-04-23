#!/usr/bin/python3

#
#module name: threeEqualSumPartitions.py
#
#purpose: given an array, determine if three partitions can be created with equal sums
#
#date created: 07/10/2020
#
#version: 1.0
#

#########################################################################################
#					import modules					#
#########################################################################################
import functools

#########################################################################################
#					function definition				#
#########################################################################################
def threeEqualSumPartitions(arr):

	#declare helper function that will check whether the sum
	#of each partition are equal
	def equalSums(sum_p1, sum_p2, sum_p3):
		if (sum_p1 == sum_p2 == sum_p3):
			return True
		else: 
			return False 

	#local variables 
	a_length = len(arr)

	#validate the input
	if a_length == 0 or a_length < 3:
		return False 

	#more local variables 
	#variables to keep track of the partitions
	left_partition_idx = 0
	right_partition_idx = a_length - 1

	#varibles to keep track of teh sums within each partition 
	left_partition_sum = arr[0]
	middle_partition_sum = functools.reduce(lambda a,b : a+b,arr[1:a_length - 1])
	right_partition_sum = arr[a_length - 1]

	#compare the three paritioins as long as the left and right 
	#parition indices do not cross 
	while left_partition_idx < right_partition_idx: 

		#check whether the three partitions are equal 
		if equalSums(left_partition_sum, middle_partition_sum, right_partition_sum): 
			return True

		#check if sum in the left partition is less than, or equal to the right one
		#add the left most element from the middle partition if sum is less
		if left_partition_sum <= right_partition_sum:
			left_partition_idx +=1
			left_partition_sum += arr[left_partition_idx]
			middle_partition_sum -= arr[left_partition_idx]
		else: #adjust the right partition (adding the right most element from the middle partition)
			right_partition_idx -= 1
			right_partition_sum += arr[right_partition_idx]
			middle_partition_sum -= arr[right_partition_idx]

	#if this point has been reached then there is no possible solution 
	return False 

#############################################################
#						main								#
#############################################################

#local variable/s
my_array = [5, 5, 5, 10, 3, 2, -6, 14]

#dsiplay note to the user
print("Checking if the below array can be partitioned in to three equal partitions")
print(str(my_array))

#check whether there were three partitions with equal sums 
if(threeEqualSumPartitions(my_array)):
	print("True")
else: 
	print("False")