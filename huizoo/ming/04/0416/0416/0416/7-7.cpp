#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	if (a >= b && a >= c) {
		cout << "MAX=" << a << endl;
		if (b >= c) {
			cout << "MIN=" << c;
		}
		else {
			cout << "MIN=" << b;
		}
	}
	else if (b >= c && b >= a) {
		cout << "MAX=" << b << endl;
		if (c >= a) {
			cout << "MIN=" << a;
		}
		else {
			cout << "MIN=" << c;
		}
	}
	else {
		cout << "MAX=" << c << endl;
		if (a >= b) {
			cout << "MIN=" << b;
		}
		else {
			cout << "MIN=" << a;
		}
	}


	return 0;
}