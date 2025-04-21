#include <iostream>
using namespace std;

void BBQ(int t)
{
	for (int x = 1; x <= t; x++) {
		cout << x;
	}
}

void KFC(char t)
{
	for (int x = 0; x < 7; x++) {
		cout << t;
	}

}



int main()
{
	int a;
	cin >> a;
	if (a % 2 != 0) {
		int b;
		cin >> b;
		BBQ(b);
	}
	else {
		char b;
		cin >> b;
		KFC(b);
	}


	return 0;
}