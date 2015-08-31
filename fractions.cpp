#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
class Fraction
{
public:
	int denom;
	int num;
	Fraction(int Num, int Denom);
};
int findGCF(int num, int denom);
void formatAndPrint(int summedNum, int commonDenom);
vector<Fraction> formatFracs(vector<Fraction> allFracs);
vector<Fraction> getFracs();
int sumNumerators(vector<Fraction> commonDenomFracs);
int main(void)
{

	int gcf;
	int commonDenom = 1;
	int summedNum = 0;
	vector<Fraction> allFracs, commonDenomFracs;
	allFracs = getFracs();
	commonDenomFracs = formatFracs(allFracs);
	summedNum = sumNumerators(commonDenomFracs);
	commonDenom = commonDenomFracs[0].denom;
	gcf = findGCF(summedNum, commonDenom);
	summedNum /= gcf;
	commonDenom /= gcf;
	formatAndPrint(summedNum, commonDenom);
	return(0);
}

int sumNumerators(vector<Fraction> commonDenomFracs)
{
	int summedNum = 0;
	for(vector<Fraction>::iterator it3 = commonDenomFracs.begin();
			it3 != commonDenomFracs.end(); it3++)
	{
		summedNum += it3->num;
	}
	return(summedNum);
}
vector<Fraction> formatFracs(vector<Fraction> allFracs)
{
	int commonDenom;
	vector<Fraction> commonDenomFracs;
	for(vector<Fraction>::iterator it = allFracs.begin();
			it != allFracs.end(); it++)
	{
		Fraction *commonDenomFrac = new Fraction(it->num,it->denom);
		for(vector<Fraction>::iterator it2 = allFracs.begin();
				it2 != allFracs.end(); it2++)
		{
			if(it == it2)
			{
				continue;
			}
			else
			{
				commonDenomFrac->denom *= it2->denom;
				commonDenomFrac->num *= it2->denom;
				commonDenom = commonDenomFrac->denom;
			}
		}
		commonDenomFracs.push_back(*commonDenomFrac);
	}
	return(commonDenomFracs);
}

vector<Fraction> getFracs()
{
	int numFracs;
	int i = 0;
	char userInputFraction[100];
	char *pch;
	vector<Fraction> allFracs;
	cout << "Enter number of fractions to be added: ";
	cin >> numFracs;
	cout << endl;
	cout << "Enter fractions in the form x/y: ";
	while(i < numFracs)
	{
		Fraction *fraction = new Fraction(1,1);
		cin >> userInputFraction;
		pch = strtok(userInputFraction, "/");
		fraction->num = atoi(pch);
		pch = strtok(NULL, ":");
		fraction->denom = atoi(pch);
		allFracs.push_back(*fraction);
		i++;
	}
	return(allFracs);
}
void formatAndPrint(int summedNum, int commonDenom)
{
	if(summedNum > commonDenom)
	{
		cout << floor(summedNum / commonDenom) << " " <<summedNum % commonDenom << "/" << commonDenom;
	}
	else
	{
		cout << summedNum << "/" << commonDenom << endl;
	}
	cout << endl;
}

int findGCF(int num, int denom)
{
	int r, temp, small, big;
	if(num > denom)
	{
		small = denom;
		big = num;
	}
	else
	{
		big = denom;
		small = num;
	}
	do
	{
		r = big % small;
		big = small;
		small = r;
	}while(r != 0);
	return(big);
}


Fraction::Fraction(int Num, int Denom)
{
	this->denom = Denom;
	this->num = Num;
}
