#
#module name: max_rooms.py
#
#purpose: Given a list of start/end times, determine the minimum number of meeting rooms that are needed
#
#date created: 07/27/2020
#
#version: 1.0
#

#########################################################################
#				import modules				#
#########################################################################
from operator import itemgetter


#########################################################################
#				function definition			#
#########################################################################
def find_min_meeting_rooms(time_slots):

	#local variables 
	meeting_times = sorted(time_slots, key=itemgetter(0))
	num_times = len(meeting_times)
	start_idx = 0
	end_idx = 0
	room_count = 0
	min_rooms_needed = 0
	currnt_start = 0
	current_end = 0

	#
	#iterate through each time (start/end time of a meeting)
	#and add a room for every start and remove a room for each 
	#end time of a meeting while always keeping track if a max
	#number of required rooms has occured
	#
	while start_idx != num_times and end_idx != num_times: 

		#assign the start and end variables 
		current_start = meeting_times[start_idx][0]
		current_end = meeting_times[end_idx][1]

		#check whether a room needs to be added 
		if current_start < current_end: 
			room_count += 1
			start_idx += 1

			#check whether this is the max number seen so far 
			min_rooms_needed = max(room_count, min_rooms_needed)
		else: # we can remove a room from the count 
			room_count -= 1
			end_idx += 1

	#retunrn the number of min rooms needed 
	return min_rooms_needed



def main():

	#local variables 
	times = [(0, 50), (30, 75), (40, 150)]
	min_rooms = 0

	#find the number of min rooms needed
	min_rooms = find_min_meeting_rooms(times)

	#display the result to the user 
	print("The min number of rooms needed is : " + str(min_rooms))


if __name__ == '__main__':
	main()
