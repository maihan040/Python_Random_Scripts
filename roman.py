#!/usr/bin/python3
'''
	roman_numerals.py

	given a roman numeral, convert it to a number

	created: 11/17/2019

	version: 1.0
'''

#import necessary modules 
import sys

#function definition
def convertRoman(s):

	#validate the string
	if len(s) < 1:
		print("Length of the string is too short, exiting now....")
		sys.exit(0)

	#define the dictionary for the roman to number mapping
	r2n = {
		'I' :[1, 3, 0],
		'IV':[4, 1, 0],
		'V' :[5, 1, 0],
		'IX':[9, 1, 0],
		'X' :[10, 3, 0],
		'XL':[40, 1, 0],
		'L' :[50, 1, 0],
		'XC':[90, 1, 0],
		'C' :[100, 3, 0], 
		'CD':[400, 1, 0],
		'D' :[500, 1, 0],
		'CM':[900, 1, 0],
		'M' :[1000, 3, 0],
	}

	#local variables
	VAL = 0
	MAX = 1
	COUNT = 2
	i = 0
	num = 0

	#debug
	char = s[0]
	print("Char is " + char)
	print("Dictionary content: " + str(r2n[char][1]))


'''
	#iterate through each character and examine it where it fits in the dictionary 
	while i < len(s) - 1:

		#grab the character 
		current = s[i]
		subStr = s[i] + s[i + 1]

		#check whether the first roman number consists of two letters
		if (subStr in r2n.keys()):
			if(r2n[subStr][COUNT] <= r2n[subStr][MAX]):
				num += r2n[subStr][VAL]
				r2n[substr][COUNT] += 1
				i += 1
			else:
				print("something went wrong")
				sys.exit(0)
		#check whether the single elemnent is in the dictionary
		elif (s[i] in r2n.keys()):
			if(r2n[s[i][COUNT]] <= r2n[s[i]][MAX]):
				num += r2n[s[i]][VAL]
				r2n[s[i]][COUNT] += 1
				i += 1
			else:
				print("something went wrong")
				sys.exit(0)
		#something went wrong
		else:
			print("something went wrong")
			sys.exit(0)

	#return the count
	return num
'''


#main 
print("Converting: MCMC")
result = convertRoman('MCMX')
print("Result is: " + str(result))