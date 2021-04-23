#!/usr/bin/python3
'''
	schedule_tasks.py

	A task is a some work to be done which can be assumed takes 1 unit of time. Between the same type of tasks you must take at least n units of time before running the same tasks again.

	Given a list of tasks (each task will be represented by a string), and a positive integer n representing the time it takes to run the same task again, find the minimum amount of time needed to run all tasks.

	created: 09/06/2020

	version: 1.0
'''

############################### Import required modules ###################################
from collections import Counter
from operator import itemgetter
################################ Function Definition ######################################
def schedule(tasks, time):
	# validation checks
	num_tasks = len(tasks)

	if num_tasks == 0 or time <= 0:
		return 0

	if num_tasks == 1:
		return num_tasks

	# additional local variables
	task_counts = Counter(tasks).most_common()  # get a list of tuples showing the unique tasks as well as their counts ordered by their frequency
	tasks_remaining = dict(sorted(task_counts, key=itemgetter(1),
								  reverse=True))  # get the keys from the above list so that we can keep track of how many still remain
	tasks = list(tasks_remaining.keys())
	time_blocks = task_counts[0][1]
	schedule = [[] for i in range(time_blocks)]  # used to hold the final propposed schedule

	# iterate for as long as there are still tasks remaining
	while tasks_remaining:
		for i in range(len(tasks)):
			schedule[i].append(tasks[0])
			tasks_remaining[tasks[0]] -= 1
			if tasks_remaining[tasks[0]] == 0:
				del (tasks_remaining[tasks[0]])
				del (tasks[0])

	# determine whether any time blocks need to have an idle slot (the last block doesn't need to be considered as
	#there is no need to idle once all tasks are completed)
	for i in range(time_blocks - 1):
		diff = time - len(schedule[i])
		if diff > 0:
			for j in range(diff):
				schedule[i].append('idle')
		else:
			continue

	#flatten the list and return its length
	final_schedule = [ task for sub_schedule in schedule for task in sub_schedule]
	print(len(final_schedule))

################################ 	Main Function	 ######################################
tasks = ['q', 'q', 'q', 'w', 'w', 's']

# call the schedule function
schedule(tasks, 4)