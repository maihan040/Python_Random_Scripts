#!/usr/bin/python3
'''
	plus_one.py

	Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.
	
	Example:
	Input: [2,3,4]
	Output: [2,3,5]


	created: 08/30/2020

	version: 1.0
'''

################################## Function Definitions ###############################
def plus_one(numbers):

	#local variables 
	n = len(numbers)
	carry = 0

	#validate the input list 
	if n == 0:
		return [1] #assuming an empty list is equivalent to [0]

	#add one to the last digit in the list 
	numbers[n - 1] += 1

	#check each digit from the last index to the first 
	for i in range(n - 1, -1, -1):

		#add the current carry to the current sum 
		numbers[i] += carry

		#check if overflow occured 
		if numbers[i] < 10:
			carry = 0
			break
		else: 
			carry = number[i] // 10
			numbers[i] %= 10

	#check if overflow occured on the first element in the list 
	if carry: 
		numbers = [1] + numbers

	#return the completed list 
	return numbers

################################## Main Function #########################################
number = []
print("Original number is : " +  str(number))
number = plus_one(number)
print("New number is : " + str(number))


