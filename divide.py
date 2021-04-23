#!/usr/bin/python3

#
# dividy.py
#
# Description: given two numbers (dividend and a divisor) divide the number without the use of any of the following operators: "+ / * %"
#
# Created: 6/03/2020
#
# Developer: codex040
#
# Version: 1.0
#

######################### Function definition ######################### 
def divide(dividend, divisor):

	#local variables
	neg = False if ((dividend < 0) and (divisor < 0) or (dividend > 0 and divisor > 0)) else True
	quotient = 0
	TOP_MIN = -2147483648
	TOP_MAX = 2147483647

	#normalize the dividend and the divisor
	dividend, divisor = abs(dividend), abs(divisor)

	#determine the quotient if the divisor isn't "0"
	if divisor != 1:
		while dividend >= divisor: 
			quotient += 1
			dividend -= divisor
	else:
		quotient = dividend

	#determine what sign needs to be assigned as well if over/underflow occured
	if neg: 
		return max(-quotient, TOP_MIN)
	else: 
		return min(quotient, TOP_MAX)


######################### Driver definition ######################### 

#local variables 
dividend = 313
divisor = 3
result = divide(dividend, divisor)

#display info to the user 
print("Dividend is : " + str(dividend))
print("Divisor is : " + str(divisor))
print("Result is : " + str(result))
