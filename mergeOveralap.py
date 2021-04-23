#!/usr/bin/python3
'''
	merge_overlap.py

	You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

	For example:
	[(1, 3), (5, 8), (4, 10), (20, 25)]

	This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

	created: 09/13/2020

	version: 1.0
'''

################################## Function Definitions ###############################
def merge_overalap(times):

	#local variables
	n = len(times)
	time_slots = sorted(times)
	merged_times = []
	i = 0
	current_time = time_slots[0]

	#iterate through the list and pick the first time slot for inspection
	#it's possible that the subsequent time/s can be merged, so hold on onto 
	#this slot until it's know for a fact that the subsequent slot can not be
	#merged with it. 
	while i < n - 1:

		if current_time[1] >= time_slots[i + 1][0]:
			start = current_time[0]
			end = max(current_time[1], time_slots[i + 1][1])
			current_time = (start, end)
			i += 1
		else:
			merged_times.append(current_time)
			current_time = time_slots[i + 1]
			i += 1

	#check if the last time slot is included in the final list
	if current_time not in merged_times:
		merged_times.append(current_time)

	#return the sorted/merged list "merged_tiems"
	return merged_times

################################## Main Function  ###############################
#local variables
times = [(1, 3), (5, 8), (4, 21), (20, 25)]

print("Times to sort are: " )
print(times)

#sort the times
merged_times = merge_overalap(times)
print("Times merged are " )
print(merged_times)