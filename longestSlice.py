def areSameSign(a, b):
	if a == 0 or b == 0 or a * b >= 0:
		return True
	else:
		return False
def checkEdge(array, index1, index2):
	if areSameSign(array[index1], array[index2]):
		return False
	else:
		return True
#check left and right, self and left, self and right
def check(array, index):
	leftAndRightOkay = areSameSign(array[index - 1], array[index + 1])
	selfAndLeftOkay = not areSameSign(array[index], array[index - 1])
	selfAndRightOkay = not areSameSign(array[index], array[index + 1])
	if leftAndRightOkay and selfAndLeftOkay and selfAndRightOkay:
		return True
	else:
		return False
def main():
	testArray1 = [5,4,-3,2,0,1,-1,0,2,-3,4,-5]
	testArray2 = [1,2,3]
	arrayLength = len(testArray1)
	sliceLength = 0
	greatestSliceLength = 0
	if checkEdge(testArray1, 0, 1):
		sliceLength += 1
		greatestSliceLength = sliceLength
	for i in range(1, arrayLength - 1):
		if check(testArray1, i):
			sliceLength += 1
		if sliceLength > greatestSliceLength:
			greatestSliceLength = sliceLength
	if checkEdge(testArray1, arrayLength -2, arrayLength -2):
		sliceLength += 1
	if sliceLength > greatestSliceLength:
		greatestSliceLength = sliceLength
	print(greatestSliceLength)
main()
