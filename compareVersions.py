#!/usr/bin/python3
#
#module name: compareVersion.py
#
#purpose: Given two software versions (represented as strings), determine which one is the most recent one 
#		  if x > y return 1
#		  if x < y return -1
#	      if they are the same, have difffernt version levels (1.0.1.1 an 1.1.0) return 0
#		  ignore leading zeroes 
#
#date created: 12/12/2019
#
#version: 1.0
#

#################################################################
#			function definition			#
#################################################################

#helper function to strip any leading zeroes
def stripLeadingZeroes(verStr):

	#Local variables
	idx = 0

	#iterate through the string until we find the first nonzero digit
	while verStr[idx] == '0':
		idx += 1

	#return only the substring that starts with a non zero digit
	return verStr[idx:]

#main function of this app
def cmpVersion(ver1, ver2):

	#local variables 
	v1 = ver1.split('.')
	v2 = ver2.split('.')

	#compare each level of the version 
	if len(v1) == len(v2):
		for (x,y) in zip(v1, v2):

			#strip leading zeroes
			if len(x) > 1 : x = stripLeadingZeroes(x)
			if len(y) > 1 : y = stripLeadingZeroes(y)

			#cmopare the two 
			if x > y: 
				return 1
			elif x < y:
				return -1 
			else:
				continue 

	return 0 # if we reach this point the versions are either the same, or the number of levels don't match 

#driver 
version1 = '1.0'
version2 = '1.0.0'
result = cmpVersion(version1, version2)
print("Result is: " + str(result))