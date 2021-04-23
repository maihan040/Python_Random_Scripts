#products.py


#import modules

import numpy

def computeProduct(nums):
	if(len(nums) > 1):
		product = numpy.prod(nums)
		products = [product/i for i in nums]
		return products


#main
numbers = [1, 3, 5]

print("Numbers are : " + str(numbers))
print("calling the compute product method")
output = computeProduct(numbers)
print("the output is: " + str(output))
