#include <iostream>
using namespace std;

int a;


void BBQ()
{
	if (a > 0 && a < 5) {
		cout << "초기값";
	}
	else if(a > 6 && a < 10) {
		cout << "중간값";
	}
	else {
		cout << "알수없는값";
	}

}

int main()
{
	cin >> a;
	if (a == 3 || a == 5 || a == 7) {
		for (int x = 1; x <= 10; x++) {
			cout << x;
		}
	}
	else if (a == 0 || a == 8) {
		for (int x = 10; x >= 1; x--) {
			cout << x;
		}
	}
	else {
		BBQ();
	}


	return 0;
}