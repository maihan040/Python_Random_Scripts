#!/usr/bin/python3
'''
	rearrange.py

	created: 11/24/2019

	version: 1.0
'''

import heapq

def rearrange(s):

	#validation check
	if len(s) <= 1:
		return s

	#populate priority queue
	pq = [(-s.count(x),x) for x in set(s)]


	#heapify the queue
	heapq.heapify(pq)

	#check whether whether it's even possible to create such an order
	#if there is a letter that occurs (n+1)/2 times, then it's not possible
	if any(-nc > (len(s) + 1)/2 for nc, x in pq):
		return ""

	#create output list
	ans = []
	while len(pq) >= 2:

		#debug
		print("Contents of the pq: ")
		print(pq)

		#grab the top two characters
		count1, char1 = heapq.heappop(pq)
		count2, char2 = heapq.heappop(pq)

		#add the characters to the list 
		ans.extend([char1, char2])

		#push the characters back to the queue if they are not 0
		if count1 + 1 : heapq.heappush(pq, (count1 + 1, char1))
		if count2 + 1:  heapq.heappush(pq, (count2 + 1, char2))

	#return the rearranged list
	return "".join(ans) + (pc[0][1] if pq else "")

#main
string = "abbccc"
print("calling function")
result = rearrange(string)
print("Result is: ")
print(result)