from random import randint
import math
def generateWords(difficultyLevel):
	words = list(open("enable1.txt").readlines())
	wordList = []
	while len(wordList) <  math.floor(difficultyLevel * 2.5):
		word = words[randint(0, len(words))]
		if len(word) != difficultyLevel + 5:
			continue
		wordList.append(word)
	for i in range(0, len(wordList)):
		wordList[i] = wordList[i].strip()
		print(wordList[i])
	return(wordList)

def displayNumCorrect(guess, word):
	numCorrect = 0
	for i in range(0, len(guess)):
		if guess[i] == word[i]:
			numCorrect += 1
	return(numCorrect)

def userGuess(word):
	word = word.lower()
	guessesLeft = 4
	while guessesLeft > 0:
		guess = input("Guess (" +  str(guessesLeft) + ")? ").lower()
		if guess == word:
			return True
		else:
			print(displayNumCorrect(guess, word), "/", len(guess), " correct")
			guessesLeft -= 1
	return False

def main():
	difficultyLevel = int(input("Enter difficulty level: "))
	wordList = generateWords(difficultyLevel)
	word = wordList[randint(0, len(wordList) - 1)]
	if(userGuess(word)):
		print("Nice job bro")
		return
	print("You suck bro")
	return

main()
