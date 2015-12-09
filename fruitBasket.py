import random
#costs is "fruit : cost"
#basket is "fruit : amount"
CostsTable = {}
def sumFruits(basket):
	totalCost = 0
	allFruits = [fruit[0] for fruit in basket]
	appearances = {fruit: 0 for fruit in allFruits}
	for fruit in basket:
		appearances[fruit[0]] += 1 
	for fruit in appearances:
		print(fruit)
		totalCost += appearances[fruit] * costs[fruit]
	return totalCost

def placeFruit(basket):
	print(basket)
	if(sumFruits(basket) > 500): #if we're over the limit, return
		basket.pop()
		return basket
	elif(sumFruits(basket) < 500): #if we're under the limit
		for fruit in costs:
			if (sumFruits(basket) + costs[fruit]) > 500:
			#if we have so many of one type of fruit we can't possibly use another
				continue
			else:
				basket.append(fruit)
		placeFruit(basket)
	else: #we've exactly hit 500 - success breh
		print(basket)
		return basket
				
def main():
	basketFile = open("fruitBasket.txt")
	basket = []
	for pair in basketFile.readlines():
		pair = pair.split(" ")
		pair[1] = int(pair[1].strip("\n"))
		fruit, cost = pair
		CostsTable[fruit] = cost
	placeFruit(basket)
	return
main()
