def conflictOnDiagonals(queensList):
	for i in range(0, len(queensList)):
		qPos = i
		q = queensList[i]
		if queenToLowerRightCollision(q, qPos, queensList) or queenToLowerLeftCollision(q, qPos, queensList):
			return(True)
		else:
			continue
	return False

def queenToLowerRightCollision(q, qPos, qList):
	for i in range(qPos, 0, -1):
		if i == qList[qPos - i] - q:
			return True

def queenToLowerLeftCollision(q, qPos, qList):
	for i in range(qPos, 0, -1):
		if -i == qList[qPos - i] - q:
			print("Does this happen")
			return True

def reject(queensList):
	#print(queensList)
	conflictingColumns = len(set(queensList)) < len(queensList)
	conflictingDiagonals = conflictOnDiagonals(queensList)
	return conflictingColumns or conflictingDiagonals

def accept(queensList):
	if len(queensList) < 8:
		return	

def main():
	n = int(input("Enter the size of the board"))
	root = []
	backtrack(root, n, 0)

def backtrack(queensList, n, start):
	#if every column has a queen, it's a solution
	if len(queensList) == n:
		print(queensList)
		return
	#otherwise search for a safe queen location
	else:
		for col in range(start, n):
			print(queensList)
			#queensList.append(col)
			if reject(queensList): #if configuration is rejected
				#start = len(queensList) - 1
				del queensList[-1] #delete the last queen
				return backtrack(queensList, n, len(queensList))
			else: #else a safe location exists
				start = len(queensList)
				queensList.append(col)
				return backtrack(queensList, n, 0)
	print("I guess it didn't find a solution")
main()
#now it gets stuck at [0, 1]
