#include <iostream>
using namespace std;

char aToZ()
{
	char a;
	cin >> a;
	if (('Z' - a) < (a - 'A')) {
		return 'Z';
	}
	else {
		return 'A';
	}
}

int main()
{
	cout << aToZ();


	return 0;
}