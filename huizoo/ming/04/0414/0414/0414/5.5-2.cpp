#include <iostream>
using namespace std;

void KFC()
{
	cout << "KFC\n";
}

void BBQ()
{
	cout << "BBQ\n";
}

int main()
{
	char str;
	cin >> str;
	if (str == 'B') {
		KFC(); 
		BBQ();
	}
	if (str == 'b') {
		BBQ();
	}
	if (str == '7') {
		KFC();
	}

	return 0;
}