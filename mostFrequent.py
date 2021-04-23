#!/usr/bin/python3
'''
	most_requent.py

	given either a string or a list of words, find the "k" most frequent words 

	created: 08/22/2020

	version: 1.0
'''

################################ function definition ########################################
def k_most_frequent_words(words, k):

	#local variables
	word_list = words.split()
	total_words = len(word_list)
	word_freq = {}
	most_freq_words = []

	#validate 
	if total_words == 0:
		return 

	#populate the dictionary with the words of the string 
	for word in word_list:

		#change the case of the word 
		word = word.lower()

		#check whether the words has already been encountered, else add it to the dictionary  
		if word in word_freq: 
			#word is already in the dictionary, increment the count 
			word_freq[word] += 1
		else: 
			#seeing a word for the first time, add it 
			word_freq[word] = 1

	#sort the values based on the occurence of the individual words 
	sorted_keys = sorted(word_freq.items(), key = lambda kv:kv[1], reverse = True)

	#filter out the "K" most frequent words 
	for i in range(k):
		most_freq_words.append(sorted_keys[i][0])

	#debug output to user 
	print("The words are: " + str(word_freq))
	print("The sorted keys are: " + str(sorted_keys))
	print("The " + str(k) + " most frequent words are : " + str(most_freq_words))


################################# main #######################################################
words_to_process = "Mercedes BMW Mercedes Audi Mercedes Porsche Porsche Lamborghini Ferrari Ferrari" 
k_most_frequent_words(words_to_process, 4)
