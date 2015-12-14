import random
#costs is "fruit : cost"
#basket is "fruit : amount"
CostsTable = {}
def sumFruits(basket):
	totalCost = 0
	for fruit in basket:
		totalCost += CostsTable[fruit]
	return totalCost

def getAmtFruitInBasket(basket):
	amounts = {fruit: 0 for fruit in basket}
	for fruit in basket:
		amounts[fruit] += 1
	return amounts


def placeFruit(basket):
	currentCost = sumFruits(basket)
	if currentCost > 500:
		basket.pop()
		placeFruit(basket)
	elif currentCost == 500:
		print("SOLUTION: ", basket)
	else:
		for fruit in CostsTable:
			if currentCost + CostsTable[fruit] > 500:
				continue
			else:
				basket.append(fruit)
				placeFruit(basket)
				
def main():
	basketFile = open("fruitBasket.txt")
	basket = []
	for pair in basketFile.readlines():
		pair = pair.split(" ")
		pair[1] = int(pair[1].strip("\n"))
		fruit, cost = pair
		CostsTable[fruit] = cost
	print(CostsTable)
	placeFruit(basket)
	return
main()
