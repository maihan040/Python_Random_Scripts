#!/usr/bin/python3

#
# excelCol.py
#
# Description: given a number, find the corresponding excel colum name
#
# Created: 12/14/2019
#
# Developer: codex040
#
# Version: 1.0
#

######################### Function definition ######################### 
def mapNumToCol(num):

	#validate the input
	if num < 0 or num > 16384:
		return None

	#local variables
	colName = ''
	baseLetter = ord('A') #get the ASCII value for 'A' which servers as t
						  #he starting point to determine all the other 
						  #characters that will be computed 

	#iterate through the num and compute the letters
	#note, after this block of code the name will be in reverse order
	#as it's starting to compute with the remainder and working its way
	#backwards to the left
	while num > 0: 
		rem = num % 26
		#check wether we have an even muliple of 26
		if rem == 0:
			colName += chr(baseLetter + 25)
			num = (num // 26 ) - 1
		else:
			colName += chr(baseLetter + rem - 1)
			num = num // 26

	#return the string, making sure to reverse it
	return colName[::-1]


######################### Driver definition ######################### 
value = 100
for i in range(1, value):
	print("Val " + str(i) + " maps to : " + mapNumToCol(i))
