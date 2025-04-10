#include <iostream>
using namespace std;

int main()
{
	int a, i, j;
	cin >> a;
	if (a > 0)
	{
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				cout << '#';
			}
			cout << endl;
		}
	}
	else
	{
		for (i = 0; i < 2; i++) {
			for (j = 0; j < 3; j++) {
				cout << '$';
			}
			cout << endl;
		}
	}

	return 0;
}