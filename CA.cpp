#include <iostream>
#include <string>
using namespace std;
char findNextState(int position, string input);
int main(void)
{
	string currentState;
	string nextState;
	cout << "Enter the input string: ";
	cin >> currentState;
	cout << currentState << endl;
	for(int i = 0; i < 25; i++)
	{
		for(int position = 0; position < currentState.length(); position++)
		{
			nextState.push_back(findNextState(position, currentState));
		}
		currentState = nextState;
		nextState = "";
		cout << currentState << endl;
	}
	return(0);	
}

char findNextState(int position, string input)
{
	string window;
	if(position > 0 && position < input.length()-1)
	{
		window = window + input[position-1] + input[position] + input[position+1];
	} // general case
	else if(position == 0)
	{
		window = window + "0" + input[position] + input[position+1];
	} // very first time
	else
	{
		window = window + input[position-1] + input[position] + "0"; 
	} // very last time

	if(window[0] == window[2])
	{
		return('0');
	}
	else
	{
		return('1');
	}
}
