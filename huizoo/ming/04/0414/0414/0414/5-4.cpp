#include <iostream>
using namespace std;

void BBQ()
{
	cout << "KFC�Դϴ�";
}

void MC()
{
	cout << "MC�Դϴ�";
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