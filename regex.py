#!/usr/bin/python3

#import necessary modules
import re

#function definitions
def checkString(string):
    
    #regex definitions
    positive_int = re.compile('^[+]?[0-9]+$')
    negative_int = re.compile('^[-][1-9]+$')
    positive_float = re.compile('^[+]?[0-9]*\.[0-9]+$')
    negative_float = re.compile('^[-][0-9]*\.[0-9]+$')
    

    if positive_int.match(string):
        print("Positive Integer")
    elif negative_int.match(string):
        print("Negative Integer")
    elif positive_float.match(string):
        print("Positive float")
    elif negative_float.match(string):
        print("Negative float")

#main
myStr = "-.3"
checkString(myStr)



