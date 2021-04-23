"""
	longestSubstr.py
	given a string, find the longest substring with no repeating characters
"""

def findLongestSubstr(textStr):

	if len(textStr) <= 1:
		return

	subStr = set(textStr[0])
	i = 1
	startPos = 0
	longestSubstrLen = 1
	longestSubstring = textStr[0]

	while i < len(textStr):
		if textStr[i] not in subStr:
			subStr.add(textStr[i])
			longestSubstring += textStr[i]
			longestSubstrLen += 1
			i += 1
		elif len(subStr) > longestSubstrLen:
			longestSubstrLen = len(subStr)
			longestSubstring = textStr[startPos: startPos + len(subStr)]
			startPos = startPos + len(subStr)
			subStr = set()
			i += 1
		else:
			i += 1

	return [longestSubstrLen, longestSubstring]


#main
myString = "abcabcadefghiabc"
print("String: " + myString)
print("Length: " + str(len(myString)))
result = findLongestSubstr(myString)
print("Longest substring length: " + str(result[0]) + " Longest substring: " + result[1])
