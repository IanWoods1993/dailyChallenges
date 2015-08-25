import math
import pdb
def main():
	spiralSize = int(input("Spiral size: "))
	pointNum = int(input("Point Number (-1 to ignore): "))
	pointLoc = [int(numeric_string) for numeric_string in input("Point Location (-1 to ignore): ").split()]
	midPoint = math.ceil(spiralSize/2)
	currPointLoc = [midPoint, midPoint]
	currPointIndex = 1
	radius = 0
	right = True
	left  = False
	down  = False
	up    = False
	#pdb.set_trace()
	while abs(radius) < math.ceil(spiralSize/2):
		if currPointIndex == pointNum:
			print(currPointLoc)
		if currPointLoc == (pointLoc):
			print(currPointIndex)
		if(right == True): #if we're moving right
			currPointLoc[0] += 1 #increment X
			if currPointLoc[0] > midPoint + abs(radius): #if we're as far right as we should be
				right = False #stop moving right
				radius += 1
				up = True #start moving up
				
		elif(up == True): #if we're moving up
			currPointLoc[1] -= 1 #decrement Y
			if currPointLoc[1] == midPoint - abs(radius):
				up = False #stop moving up
				left = True #start moving left
		
		elif(left == True): #if we're moving left
			currPointLoc[0] -= 1 #decrement x
			if currPointLoc[0] == midPoint - abs(radius):
				left = False
				down = True

		elif(down == True):
			currPointLoc[1] += 1
			if currPointLoc[1] == midPoint + abs(radius):
				down = False
				right = True
		currPointIndex += 1
	return

main()


