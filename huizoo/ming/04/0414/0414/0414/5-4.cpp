#include <iostream>
using namespace std;

void BBQ()
{
	cout << "KFC입니다";
}

void MC()
{
	cout << "MC입니다";
}

int main()
{
	int a;
	cin >> a;
	if (a == 1) {
		BBQ();
	}
	else {
		MC();
	}

	return 0;
}