#sort.py
#given an array which consists of three unique values, sort them in 
#increasing order


########################################################################
#Function definitions
########################################################################
def sortNums(nums):
	
	#check if there are any number to process
	if(len(nums) == 0):
		return []
		
	#local variables
	numbers = []
	unique_values = {}
	
	#iterate through the list and categorize the values
	for num in nums:
		if(num not in unique_values.keys()):
			unique_values[num] = []
		unique_values[num].append(num)

	#append the three indiividual lists into the main "number" one
	#and return the list
	for k in sorted(unique_values.keys()):
		numbers += unique_values[k]
	
	#return the list 
	return numbers
	

########################################################################
#Main function
########################################################################
numbers = [2, 1, 2, 1, 2, 1, 3, 3, 3, 2, 1]
print("Initial list: ")
print(numbers)
print("Sorting the numbers....")
sorted_numbers = sortNums(numbers)
print("Sorted list: " )
print(sorted_numbers)
