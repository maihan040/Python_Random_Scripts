#!/usr/bin/python3

#
#recoverIpAddress.py
#
# Description: given a string which represents an ip address, find the 
#			   possible list of valid ip addresses
#
# Created: 12/17/2019
#
# Developer: codex040
#
# Version: 1.0
#

######################### Import Modules ######################### 
from datetime import datetime 

######################### Function definition ######################### 

#Helper Function
def checkIP(ipAddr):
	ip = ipAddr.split('.')

	#iterate throuch each octet and determine whether it's valid
	for octet in ip: 
		if int(octet) < 0 or int(octet) > 255:
			return None
		if len(octet) > 1 and int(octet) == 0:
			return None
		if len(octet) > 1 and octet[0] == '0':
			return None

	#valid ip address at this point
	return True


#core function 
def recoverIP(ip):
	iplen =  len(ip)

	#validate the input
	if iplen < 4 or iplen > 12:
		return None

	#local variables
	ipList = []
	maxIplen = iplen + 3

	#iterate through the list and place the dots in various positions of the string to see if that will result in a valid ip address
	for i in range(1, 4):
		for j in range(1, 4):
			j = j + i 
			for k in range(1, 4):
				k = k  + j

				#build a temp string consisting of the IP which includes the dots placed within it
				tempIp = ip[:i] + "." + ip[i:j] + "." + ip[j:k] + "." + ip[k:]

				#find the location of the last ".". This will be used to validate whether the IP makes logical sense
				lastDot = tempIp.rfind(".")

				#check
				if lastDot + 4 < maxIplen:
					continue
				else: 
					ipList.append(tempIp) if checkIP(tempIp) else "" 

	#return the list 
	return ipList


#driver. Press Play 
startTime = datetime.now()
possibleIPAddresses = recoverIP("1592551013")
endTime = datetime.now()
if possibleIPAddresses: 
	print("Posible IP address/es : " + str(possibleIPAddresses))
	print("Time taken: " +str(endTime - startTime))
