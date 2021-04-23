#
#module name: validate_parenthesis.py
#
#purpose: given a string of opening and closing parenthesis "{}, [], ()", write a code that checks they are properly closed. 
#		  i.e. simulate the compiler checking a source code for proper usage of the parenthesis
#
#date created: 07/21/2020
#
#version: 1.0
#

############################### function definition #####################################
def validate_parenthesis(source_code): 

	#
	#local variables
	#

	#check for zero length and return true as that's technically matching
	str_len = len(source_code)
	if str_len == 0:
		return True 

	#variables to help keep track of opening parenthesis, as well as a look up table 
	p_idx = 0
	p_stack = [] 
	p_look_up = { '}' : '{', ']' : '[', ')' : '('}
	open_parenthesis = ('(', '[', '{')
	close_parenthesis = (')', ']', '}')

	#iterate through the "source code" and check for any opening/closing parenthesis
	for i in range(str_len): 

		#
		#check possible outcomes 
		#

		if source_code[i] in open_parenthesis: #case of encounering an opening parenthesis
				p_stack.append(source_code[i])
				p_idx += 1
		elif source_code[i] in close_parenthesis: #case of encountering closing parenthesis
			if p_look_up[source_code[i]] == p_stack[p_idx - 1]: 
				p_stack.pop()
				p_idx -= 1
			else: #found a mismatch 
				return False
		else: #continue 
			continue 

	#check whether the "p_stack" list is completely empty, which would indicate that all encountered 
	#parenthesis match 
	return True if len(p_stack) == 0 else False
 
###################################### MAIN ##############################################
def main():

	my_source_code = "[{{{{{{{{{}}}}}}}}()()()]"
	print("Following strin will be checked: " + my_source_code)
	print(validate_parenthesis(my_source_code))


################################## trigger code ##########################################
if __name__ == "__main__": 
	#excecute main 
	main()