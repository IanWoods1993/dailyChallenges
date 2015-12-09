#PROBLEMS: QUEENSLIST IS USUALLY NOT OF MAX SIZE

def checkDiagonals(queensList):
	for q in queensList:
		qPos = qList.index(q)
		return queenToUpperRight(q, qPos, queensList) and queenToUpperLeft(q, qPos, queensList)

def queenToUpperRight(q, qPos, qList):
	for i in range(1, len(qList)):
		if qPos + i >= len(qList):
			continue
		if q + i == qList[qPos + i]:
			return False

def queenToUpperLeft(q, qPos, qList):
	for i in range(1, len(qList)):
		if qPos + i >= len(qList):
			continue
		if q - i == qList[qPos + i]:
			return False

#def checkDiagonals(queensList):
#	positions = []
#	for i in range(0,len(queensList)):
#							#(row, column)
#		position = (i, queensList[i])
#		positions.append(position)
#	print(positions)
#	for position in positions:
#		if checkLowerLeftToUpperRight(position, positions) and checkLowerRightToUpperLeft(position, positions):
#			return True
#	return False	

def checkLowerLeftToUpperRight(position, positions):
	row = position[0]
	column = position[1]
	diagNum = row + column
	for diagIndex in range(max(0, diagNum - len(positions)), min(diagNum, len(positions))):
		x = diagIndex
		y = diagNum - diagIndex
		if (x,y) in positions:
			return False #interferes with another queen
	return True

def checkUpperLeftToLowerRight(position, positions):
	row = position[0]
	column = position[1]
	diagNum = row + column
	#maintainedfor diagIndex in range(max(0, diagNum - len(positions)), min(diagNum + 1, len(positions))):
		x = diagIndex
		y = diagNum - diagIndex
		if (x, y) in positions:
			return False
	return True
		
def reject(queensList):
	sameColumn = len(set(queensList)) < len(queensList)
	result = []
	checkDiagonals(queensList)
		#write it to do scans across diagonals - like, scan (1,1), then [(1,2), (2,1) etc
	#result.append(queensList.index(i) - i) #find difference between (x, y), finds lower-left to upper-right diagonals
		
	sameDiagonal = len(set(result)) < len(queensList)
	return(True)
	return(False)

def accept(queensList):
	if len(queensList) < 8:
		return	

def main():
	root = [0]
	backtrace(root)

def backtrace(queensList):
	if reject(queensList):
		return
	if accept(queensList):
		output(queensList)
	extension = generateExtension(queensList)
	return
main()
