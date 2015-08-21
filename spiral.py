import math
def main():
	spiralSize = int(input("Spiral size: "))
	pointNum = int(input("Point Number: "))
	midPoint = math.ceil(spiralSize/2)
	currPoint = [midPoint, midPoint]
	print(currPoint)
	i = 0
	right = True
	left = False
	down = False
	up = False
	while math.fabs(i) < math.ceil(spiralSize/2):
		if(right == True): #if we're moving right
			i = i + 1
			currPoint[0] = currPoint[0]+1 #increment X
			if currPoint[0] == midPoint + math.fabs(i): #if we're as far right as we should be
				right = False #stop moving right
				up = True #start moving up
				
		elif(up == True): #if we're moving up
			currPoint[1] = currPoint[1]-1 #decrement Y
			if currPoint[1] == midPoint - math.fabs(i):
				up = False #stop moving up
				left = True #start moving left
		
		elif(left == True): #if we're moving left
			currPoint[0] = currPoint[0]-1 #decrement x
			if currPoint[0] == midPoint - math.fabs(i):
				left = False
				down = True

		elif(down == True):
			currPoint[1] = currPoint[1] + 1
			if currPoint[1] == midPoint + math.fabs(1):
				down = False
				right = True
		
		print(currPoint)
		print("i is : ", i)
	return

main()



#c  , c
#c+1, c
#c+1, c-1
#c  , c-1
#c-1, c-1
#c-1, c
#c-1, c+1
#c, c+1
#c+1, c+1
#c+2, c+1
#c+2, c
#c+2, c-1
#c+2, c-2

