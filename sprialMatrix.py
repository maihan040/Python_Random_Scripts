#
#module name: sprialMatrix.py
#
#purpose: Given a two d matrix, print the matrix in a sprial fashion
#
#date created: 10/06/2019
#
#version: 1.0
#


#################################################################################
#				import libraries				#
#################################################################################
import math

#################################################################################
#				function definition				#
#################################################################################

#helper function  to print the matrix
def printMatrix(matrix):

	#validation check
	if len(matrix) <= 0:
		return 

	#print the matrix row by row, right justified with 3 spaces for each number
	for row in matrix:
	    for val in row:
	        print (str(val).rjust(3) + " ", end='')
	    print()

#core function of the program to print the matrix in spiral order
def printSprialMatrix(matrix): 

	#validation check 
	if len(matrix) <= 0:
		return

	#local variables
	odd =1 if len(matrix) % 2 == 1 else 0

	#loop over the matrix 
	for row in range(0, math.floor(len(matrix)/2), 1):

		#common expression
		current_limit = len(matrix[row]) - (row + 1)

		#############################################################
		#		Print the numbers going in the right direction		#
		#############################################################
		for r in range(row, current_limit):
			print(str(matrix[row][r]).rjust(3) + " ", end='')
		
		#############################################################
		#		Print the numbers going in the down direction		#
		#############################################################
		for d in range(row, current_limit):
			print(str(matrix[d][current_limit]).rjust(3) + " ", end='')

		#############################################################
		#		Print the numbers going in the left direction		#
		#############################################################
		for l in range(current_limit, row, -1):
			print(str(matrix[current_limit][l]).rjust(3) + " ", end='')

		#############################################################
		#		Print the numbers going in the up direction			#
		#############################################################
		for u in range(current_limit, row, -1):
			print(str(matrix[u][row]).rjust(3) + " ", end='')


	#print the center value if the matrix has odd dimeions
	if(len(matrix)%2 == 1):
		print(str(matrix[math.floor(len(matrix)/2)][math.floor(len(matrix)/2)]).rjust(3))

	#return 
	return

#############################################################
#							Main							#
#############################################################

#local variables
myMatrix = [[1, 2, 3, 4, 5],
		    [6, 7, 8, 9, 10],
		    [11, 12, 13, 14, 15],
		    [16, 17, 18, 19, 20],
		    [21, 22, 23, 24, 25]]


#debug
print("Printing the original matrix: ")
printMatrix(myMatrix)
print("Printing the matrix in sprial order: ")
printSprialMatrix(myMatrix)