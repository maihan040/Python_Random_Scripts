#two_sum.py
#given a list and a target "k" find if there are two numbers in the list
#that can add up to the target

#function definition
def two_sum(list, k):
	#iterate through the list and check if a pair exists
	for i in range(0,len(list)): 
		diff = k - list[i]
		if diff in list[i:]:
			return True

	#at this point there is no pair that can add up to the target
	return False


#main
nums = [4, 7, 1, -3, 2]
target = 6


print("List is: ")
print(list)
print("Target is: " + str(target))
print("Searching ..... ")
result = two_sum(nums, target)
print("Has pair : " + str(result))
