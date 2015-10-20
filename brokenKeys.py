import sys
def main():
	words = str(open("enable1.txt").readlines()).rstrip('\n')
	print(words)
	numLines = int(input())
	keys = []
	for i in range(0, numLines):
		keys.append(input())

	for element in keys:
		letters = set(list(element))
		print(letters)

main()
