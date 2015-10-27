class Suitor:
	def __init__(self, n, s, po, pa):
		self.name = n
		self.status = s
		self.partnerOrder = po
		self.partnersAsked = pa
def getSuitorFromText(line):
	suitorName = line[0]
	suitorStatus = 0
	suitorPartnerOrder = list(line[1:].strip('\n').replace(',','').replace(' ',''))
	suitorPartnersAsked = []
	suitor = Suitor(suitorName, suitorStatus, suitorPartnerOrder, suitorPartnersAsked)
	return suitor
def main():
	manList = []
	womanList = []
	with open("stableMarriage.txt") as f:
		for line in f:
			if(line[0].upper() != line[0]):
				womanList.append(getSuitorFromText(line))
			else:
				manList.append(getSuitorFromText(line))
main()
