#!/usr/bin/python3
'''
	binary search 

	implement binary search 

	created: 09/03/2020

	version: 1.0
'''

######################## Function Definition ####################
def binary_search(numbers, target, is_sorted = False):

	#local variables 
	s = 0 #start of the list 
	e = len(numbers) - 1 #end of the list 
	
	#sort the numbers if they are not already sorted 
	if is_sorted != True:
		numbers.sort()		

	#validation check 
	if e < 0: 
		return -1 #indicate the number which was 
				  #searched for doesn't exist in the current list 
	
	#iterate through each respective section of the list and 
	#check whether the number to be searched for is there 
	while s < e: 
		m = (s + e) // 2

		#perform checks
		if numbers[m] < target: 	#need to check right side 
			s = m + 1
		elif numbers[m] > target:	#need to check left side
			e = m - 1
		else: 						#found the number 
			return m

	#at this point, s == e and it's possible it will match 
	#the number tha is being searched 
	if numbers[s] == target: 
		return s 
	else: 
		return -1 