class Suitor:
	def __init__(self, n, s, po, pa):
		self.name = n
		self.status = s
		self.partnerOrder = po
		self.partnersAsked = pa

def getSuitorFromText(line):
	suitorName = line[0]
	suitorStatus = "free"
	suitorPartnerOrder = list(line[1:].strip('\n').replace(',','').replace(' ',''))
	suitorPartnersAsked = []
	suitor = Suitor(suitorName, suitorStatus, suitorPartnerOrder, suitorPartnersAsked)
	return suitor

def moreToProposeTo(suitorsList, oppositeSuitorsList):
	oppositeNamesList = [suitor.name for suitor in oppositeSuitorsList]
	askedList = [suitor.partnersAsked for suitor in suitorsList]
	for asked in askedList:
		if set(asked) != set(oppositeNamesList):
			return(True)
	return(False)

def matchSuitors(suitorsLists):
	menList, womenList =  suitorsLists[0], suitorsLists[1]
	finalMatchups = []
	for man in menList:
		i = 0
		while man.status == "free" and moreToProposeTo([man], womenList):
			w = man.partnerOrder[i]
			for woman in womenList:
				if woman.name == w and woman.status == "free":
					man.status = woman.name
					woman.status = man.name
				else:
					if woman.status != "free":
						if woman.partnerOrder.index(man.name) < woman.partnerOrder.index(woman.status):
					#man woman is engaged to becomes free
							for engagedMan in menList:
								if engagedMan.name == woman.status:
									engagedMan.status = "free"
							man.status = woman.name
							woman.status = man.name
			i = i + 1
		finalMatchups.append([man.name, man.status])
	print(finalMatchups)
					#else they remain engaged
						
def main():
	manList = []
	womanList = []
	with open("stableMarriage2.txt") as f:
		for line in f:
			if(line[0].upper() != line[0]):
				womanList.append(getSuitorFromText(line))
			else:
				manList.append(getSuitorFromText(line))
	suitorsLists = [manList, womanList]
	matchSuitors(suitorsLists)
main()
