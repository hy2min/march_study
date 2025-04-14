#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	if (a > 5) {
		for (int x = 1; x <=10; x++) {
			cout << x << endl;
		}
	}
	else {
		for (int x = 5; x >= 1; x--) {
			cout << x << endl;
		}
	}





	return 0;
}