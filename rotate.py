#!/usr/bin/python3

#
# rotate.py
#
# Description: given a list of numbers, and an integer 'k', rotate the list  left by 'k' spots
#
# Created: 6/01/2020
#
# Developer: codex040
#
# Version: 1.0
#

###################### Import necessary modules ######################
import numbers 

######################### Function definition ######################### 

def rotateArray(arr, k): 

	# [1, 2, 3, 4, 5, 6, 7] k = 2
	# [6, 7, 1, 2, 3, 4, 5]

	#local variable 
	length = len(arr) 

	#rotate the array via concatenating two arrays conposed by slicing 
	#the original one 
	if length: 
		print("Array is : " + str(arr))
		arr = arr[length - k:] + arr[0: length - k]
		print("Now array is: " + str(arr))
	else: 
		return 


######################### Main functino  ######################### 
#local variable
my_Array = [1, 2, 3, 4, 5, 6, 7, 8]
k = 0

#display the original list 
print("Contents of the list prior to rotating it: " + str(my_Array))

#ask user for the number by which it should rotate the list
#also validate the input via a "do while" fashion 
while True: 
	k = input("Enter a number by which the list should be rotated !")

	print("k is of type: " + str(type(k)))
	if isinstance(int(k), numbers.Number):
		break

#rotate the method after having validated the user input 
rotateArray(my_Array, int(k))

#display the rotated list 
print("Contents of the rotated list are: " + str(my_Array))
