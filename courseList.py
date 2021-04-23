#!/usr/bin/python3

#
#module name: courseList.py
#
#purpose: determine the order of courses that need to be taken based on their prerequisites of them.
#		  The courses, along with their prerequisites will be passed a as a dictionary 
#
#date created: 10/03/2019
#
#version: 1.0
#

#################################################################
#			function definition			#
#################################################################
def prerequisites(course):

	#validation check 
	if courses ==  None:
		print("No courses were passed")

	#local variables
	course_list = []

	#iterate through the dicionary until there are no more classes left
	#based on the prerequisites 
	for i in range(0, len(courses)): 
		print()
		for k,v in courses.items():
			if v == course_list:
				course_list.append(k)

	#print the order to take the courses
	print("Courses should be taken in the following order: " + str(course_list))

#################################################################
#				Main				#
#################################################################

#local variable
courses = {
	'csc400' : ['csc100', 'csc200', 'csc300'],
	'csc300' : ['csc100', 'csc200'],
	'csc200' : ['csc100'],
	'csc100' : []
}

#call function to print the list in order
prerequisites(courses)
