import sys
def main():
	words = open("enable1.txt").readlines()
	wordList = []
	for word in words:
		wordList.append(word.strip('\n'))
	numLines = int(input())
	keys = []
	for i in range(0, numLines):
		keys.append(input())
	for key in keys:
		longestWord = ""
		lettersInKey = set(key)
		for word in wordList:
			lettersInWord = set(word)
			if lettersInWord.issubset(lettersInKey) and len(longestWord) < len(word):
				longestWord = word
		print(key, longestWord)
			

main()
