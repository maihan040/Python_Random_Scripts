#!/usr/bin/python3

#
#module name: findFixedPt.py
#
#purpose: Given a list of values, find the fixed point, i.e. point where the index is also the value contained at the index
#
#date created: 12/30/2019
#
#version: 1.0
#

#################################################################
#			import modules				#
#################################################################
import time

#################################################################
#			function definition			#
#################################################################
def findFixedPt(arr, low, high):

	#loop through the array 
	while low <= high: 
		#define the midpoint
		mid = (low + high)//2
		if arr[mid] == mid:
			return 1
		elif arr[mid] < mid: 
			low = mid + 1
		else: 
			high = mid - 1

	#should this point be reached then it means there is no fixed index
	return None



	''' Recursive method
	#base case
	if low > high: 
		return None
	else: #split the array into to and use binary search to find the index
		#find the mid point
		mid = (low + high)//2
		#check the midpoint
		if arr[mid] == mid: 
			return 1
		elif arr[mid] < mid:
			return findFixedPt(arr, mid + 1, high)
		else: 
			return findFixedPt(arr, low, mid - 1)
	'''

def findFixedPtBruteForce(arr):
	idx = 0
	length = len(arr)

	while idx < length:
		if arr[idx] == idx:
			return 1
		idx +=1

	#nothing found
	return None


#############################################################
#					main function 							#
#############################################################
myList = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13]

print("Result via binary search approach")
start = time.time()
result = findFixedPt(myList, 0, len(myList) - 1)
end = time.time()
if result:
	print("Result is: " + str(result))
else: 
	print("No such index exists")
print("Elapsed time: " + str((end - start)) + " seconds")

print("Result via brute force approach")
start = time.time()
result = findFixedPtBruteForce(myList)
end = time.time()
if result:
	print("Result is: " + str(result))
else: 
	print("No such index exists")
print("Elapsed time: " + str((end - start)) + " seconds")

