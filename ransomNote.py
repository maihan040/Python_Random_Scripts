#!/usr/bin/python3
'''
	ransom_note.py

	A criminal is constructing a ransom note. In order to disguise his handwriting, he is cutting out letters from a magazine.

	Given a magazine of letters and the note he wants to write, determine whether he can construct the word.

	created: 09/04/2020

	version: 1.0
'''

############################### Import required modules ###################################
from collections import Counter

################################ Function Definition ######################################
def ransom_note(magazine, note): 

	#validate the input 
	if len(magazine) == 0 or len(note) == 0:
		return False

	#create two counters to see how many letters are in the magazine and the note 
	mag_count = Counter(magazine)
	note_count = Counter(note)
	
	#check for each required letter 
	for letter in note_count:

		#check the current letter 
		if note_count[letter] > mag_count[letter]: 
			return False
		else: 
			continue

	#if this point has been reached it means that the magazine does contain enough 
	#letters to generate the note 
	return True

########################################### Main ###########################################

#local varaibles 
magazine = ['a', 'b', 'c', 'd', 'e', 'f']
note = 'bed'
result = ransom_note(magazine, note)

#display the result 
if(result): 
	print("The note can be generated")
else: 
	print("The note can not be generated")