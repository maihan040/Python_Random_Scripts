#!/usr/bin/python3

def change_int(num):
    num += 5
    print("Inside the function with num changed to : " + str(num))


#main
myNum = 5
print("Inside the main function with num being: " + str(myNum))
print("calling the change int function")
change_int(myNum)
print("now my int is : " + str(myNum))
