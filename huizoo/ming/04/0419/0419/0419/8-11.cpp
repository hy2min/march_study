#include <iostream>
using namespace std;

int a;

void starBox()
{
	for (int x = 0; x < 20; x++) {
		if (x % 2 == 1) {
			cout << x << ' ';
		}
	}
}

void macDoll() {
	for (char x = 'H'; x >= 'A'; x--) {
		cout << x << ' ';
	}
}

void copyBean() {
	for (int x = -5; x <= 5; x++) {
		cout << x << ' ';
	}
}



int main()
{
	cin >> a;
	if (a >= 3500 && a <= 5000) {
		starBox();
	}
	else if (a >= 2500 && a < 3500) {
		macDoll();
	}
	else {
		copyBean();
	}


	return 0;
}