#include <iostream>
using namespace std;

int main()
{
	int a, b, x;
	cin >> a >> b;
	if (a > b)
	{
		for (x = 0; x < 4; x++)
		{
			cout << a;
		}
	}
	else
	{
		for (x = 0; x < 4; x++)
		{
			cout << b;
		}
	}


	return 0;
}