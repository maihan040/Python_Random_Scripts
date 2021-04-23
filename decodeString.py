#!/usr/bin/python3
'''
	decode_string.py

	Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 
	3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

	created: 08/24/2020

	version: 1.0
'''

################################ function definition ########################################
def decode_string(string):

	#local variables 
	str_length = len(string)
	digits = [] #keep track of any digits that are encountered
	chars = [] #keep track of any chars that were encountered 
	i = 0

	#validate the input 
	if str_length == 0:
		return ''

	#iterate through the entire string 
	while i < str_length:

		#first case, the encountered character is a letter or an opening bracket i.e '['
		if string[i].isalpha() or string[i] == '[':
			chars.append(string[i])
			i += 1

		#second chase, the encountered character is a digit
		elif string[i].isdigit():
			num = []

			#number could be more than just a single digit
			#this block will compute the number
			while string[i].isdigit():
				num.append(string[i])
				i += 1

			#convert the number to a string and append it to the "digits" list
			number = ''.join(num)
			digits.append(int(number))

		#third and final case, encountering ']'
		else: 
			temp = ''

			#trace back until the most recent openeing bracket to compute the sub string
			while(1):
				temp += chars[-1]
				chars.pop()

				if chars[-1] == '[':
					chars.pop()
					break

			#add the new deoded string  to the chars list 
			chars.append(digits[-1] * temp[::-1])
			digits.pop()
			i += 1
	
	#return the decoded string 
	return chars[0]

############################# main #######################################

#local variables 
test_string = '2[a2[b]c]'
decoded_string = decode_string(test_string)

print("Original : " + test_string)
print("Decoded  : " + decoded_string)
