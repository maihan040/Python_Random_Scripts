#!/usr/bin/python3

#
# ipAddrGenerator.py
#
# Description: given a string which represents an ip address, find the 
#			   possible list of valid ip addresses
#
# Created: 12/14/2019
#
# Developer: codex040
#
# Version: 1.0
#

######################### Import Modules ######################### 
from datetime import datetime 

######################### Function definition ######################### 

#Helper Function#
def isIPValid(ipAddress):
	ipAddr = ipAddress.split('.')

	#check whether any octet fails a corner case
	for octet in ipAddr:
		if len(octet) > 3 or int(octet) < 0 or int(octet) > 255:
			return False
		if len(octet) > 1 and int(octet) == 0:
			return False
		if len(octet) > 1 and int(octet) > 0 and octet[0] == '0':
			return False

	#at this point all the corner cases have been validated and the string is valid
	return True

#core function 
def convertIP(ipAddress): 
	#local variables
	size = len(ipAddress)

	#validate the size
	if size < 4 or size > 12: 
		return []

	#local variables
	s = ipAddress #temp string 
	ipList = []

	#place three periods throughout the strings and check whether the resulting ip address is valid
	for i in range(1, size - 2):
		for j in range(i + 1, size - 1):
			for k in range(j + 1, size):
				s = s[:k] + "." + s[k:]
				s = s[:j] + "." + s[j:]
				s = s[:i] + "." + s[i:]

				#check whether the current ip address is valid
				if isIPValid(s):
					ipList.append(s)

				#reset the temp string to try another address
				s = ipAddress

	#return the list
	return ipList

#driver
startTime = datetime.now()
ipList = convertIP("1592551013")
endTime = datetime.now()
print("Possible ip addresses: " + str(ipList))
print("Time taken: " +str(endTime - startTime))