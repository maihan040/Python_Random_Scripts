#!/usr/bin/python3

#
# longestRun.py
#
# Description: given a number, find the longest sequence of 1s given its binary representation
#
# Created: 12/14/2019
#
# Developer: codex040
#
# Version: 1.0
#

######################### Function definition ######################### 
def longestRun(num):
    # validate the input
    if num < 1:
        return 0

    # 1 convert the num to binary and get a string representation. Make sure to remove the leading two characters '0b'
    # 2 Pick the max sequence of 1s
    # 3 Return the length of that sequence 
    return len(max((bin(num)[2:]).split('0'), key=len))


    ''' First solution 
    # local variables
    longestSoFar = 0
    currentRun = 0

    # iterate through each bit and check whethe it's a "0" or a "1"
    while num:
        if num & 1:
            currentRun += 1
        else:
            longestSoFar = max(longestSoFar, currentRun)
            currentRun = 0
        num = num >> 1

    # check the last iteration
    longestSoFar = max(longestSoFar, currentRun)

    # return the longest seen sequence
    return longestSoFar
    '''

######################### Driver Code #########################
number = 446
print("Longest seen sequence is : " + str(longestRun(number)))
