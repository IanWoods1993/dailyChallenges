import sys
import time
from functools import reduce
from operator import mul
from operator import add
from itertools import combinations_with_replacement
def main():
	startTime = time.time()
	vampLength = int(sys.argv[1])
	numFangs = int(sys.argv[2])
	#lowerBound = int(10**((vampLength / 2) - 1))
	#upperBound = int(10**(vampLength / 2))
	#possibleFangs = range(lowerBound, upperBound)
	possibleFangs = range(10, 100)
	for factors in combinations_with_replacement(possibleFangs, numFangs):
		num = reduce(mul, factors)
		numNums = sorted(list(str(num)))
		temp = sorted(map(list, (map(str, factors))))
		factorNums = sorted([val for sublist in temp for val in sublist])
		#print(numNums)
		if numNums == factorNums:
			print(factors, num, "<-- vampire!")
	print(time.time() - startTime)
	return

main()
