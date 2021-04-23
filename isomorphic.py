#!/usr/bin/python3

from collections import defaultdict
import time


def isIsomorphic(s,t):

		#validate
		m, n = len(s), len(t)
		if m != n:
			return False

		mapping = {}

		for i in range(m):
			if s[i] not in mapping:
				if t[i] in mapping.values():
					return False
				else:
					mapping[s[i]] = t[i]
			elif mapping[s[i]] == t[i]:
				continue
			else:
				return False

		return True

#main 
string1 = "egg"
string2 = "add"

start = time.time()
result = isIsomorphic(string1, string2)
end = time.time()
if(result):
	print("Isomorphic")
else:
	print("not isomorphic")
print("elapsed time: " + str(end - start))


