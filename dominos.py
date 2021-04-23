#!/usr/bin/python3
'''
	fallingDominos.py

	created: 11/22/2019

	version: 1.0
'''

def fallingDominos(dominos):

	symbols = [(i,x) for i, x in enumerate(dominos) if x != '.']
	symbols = [(-1, 'L')] + symbols + [(len(dominos), 'R')]

	ans = list(dominos)

	for (i,x), (j,y) in zip (symbols, symbols[1:]):
		#DEBUG
		print("Value of i is: " + str(i))
		if x == y:
			for k in range(i + 1, j):
				ans[k] = x
		elif x > y:
			for k in range(i + 1, j):
				ans[k] = '.LR'[cmp(k - i, j - k)]


	return "".join(ans)


def cmp(a, b):
	print("Comparing : " + str(a) + " with : " + str(b))
	return (a > b) - (a < b)


#main

print("Inside the main method")
dominos = "..R..L.R..R.."
print("Initial: " +  dominos)
final = fallingDominos(dominos)
print("Final : " + final)