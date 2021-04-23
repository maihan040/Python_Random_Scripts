#!/usr/bin/python3

#import pyenchant

def letter_combinations(digits):

	#validate
	if len(digits) == 0: 
		return []

	#variales
	letters = {
		'2' : ['a', 'b', 'c'],
		'3' : ['d', 'e', 'f'], 
		'4' : ['g', 'h', 'i'], 
		'5' : ['j', 'k', 'l'],
		'6' : ['m', 'n', 'o'], 
		'7' : ['p', 'q', 'r', 's'], 
		'8' : ['t', 'u', 'v'],
		'9' : ['w', 'x', 'y', 'z']
	}

	output = []

	#helper function
	def generate(comb, next_digit):
		#base case
		if len(next_digit) == 0:
			output.append(comb)
		else: 
			for letter in letters[next_digit[0]]: 
				generate(comb + letter, next_digit[1:])


	#call the helper function 
	generate('', digits)
	return output


#main 
result = []
print("Generating all the possible combinations")
result = letter_combinations("364")
print("The result is: " +str(result))
