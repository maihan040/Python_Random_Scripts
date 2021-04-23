#
#module name: witnesses.py
#
#purpose: There are n people lined up, and each have a height represented as an integer. 
#A murder has happened right in front of them, and only people who are taller than everyone 
#in front of them are able to see what has happened. How many witnesses are there?
#
# 36341 x (murder scene)
#
#date created: 10/05/2019
#
#version: 1.0
#

#########################################################################################
#				import libraries					#
#########################################################################################
import sys

#########################################################################################
#				function definition					#
#########################################################################################
def witnesses(people):

	#list validation check
	if len(people) <= 1:
		return people; 

	#local variables
	witness_list = []
	maxHeightSoFar = (-sys.maxsize - 1)
	people_count = len(people)

	#iterate through the people and look for an upwared trend in height
	#it's assumed the crime happened at the right, so the iteration happens 
	#from the end of the list
	for i in range(people_count - 1, 0, -1):
		if(people[i] > maxHeightSoFar):
			maxHeightSoFar = people[i]
			witness_list.append(people[i])

	#reverse the list of the witnesses to match the provided order
	witness_list.reverse()
	return witness_list

#########################################################################################
#					Main						#
#########################################################################################

#local variables
height = [3, 6, 3, 4, 1]

print("Height of peoples present: " + str(height))
print("Witnesses are: " )
witness_list = witnesses(height)
print(str(witness_list))