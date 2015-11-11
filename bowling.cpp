#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;
vector<vector<int>> processInput(string input);
int strike(int next, int last);
int spare(int next);
int hit(int curr);

int main(void)
{
	int score = 0;
	string input = "X X X X X X X X X XXX";
	//string input2 = "X -/ X 5- 8/ 9- X 81 1- 4/X";
	//string input3 = "62 71  X 9- 8/  X  X 35 72 5/8";
	vector<vector<int>> processedInput = processInput(input);
	/*for(int i = 0; i < input.length(); i++)
	{
		if(input[i] == 'X')
		{
			score += strike(input[i+1], input[i + 2]);
		}
		else if (input[i] == '/')
		{
			score += spare(input[i+1]);
		}
		else
		{
			score += hit(input[i]);
		}
	}*/
	return(0);
}

vector<vector<int>> processInput(string input)
{
	int outerArrayIndex = 0;
	int innerArrayIndex;
	vector<vector<int>> processedInput;
	for(int i  = 0; i < input.length(); i++)
	{
		innerArrayIndex = 0;
		if(input[i] == ' ')
		{
			outerArrayIndex++;
		}
		if(input[i] == 'X')
		{
			processedInput[outerArrayIndex][innerArrayIndex] = 10;
			innerArrayIndex++;
		}
		else if(input[i] == '/')
		{
			processedInput[outerArrayIndex][innerArrayIndex] = 10 - input[i-1] - '0';
			innerArrayIndex++;
		}
		else
		{
			processedInput[outerArrayIndex][innerArrayIndex] = input[i] - '0';
			innerArrayIndex++;
		}
	}
	return(processedInput);
}

int strike(int next, int last)
{
	return(10 + 2*next + 2*last);
}

int spare(int next)
{
	return(10 + next);
}

int hit(int curr)
{
	return(curr);
}

