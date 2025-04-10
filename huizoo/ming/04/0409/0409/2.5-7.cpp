#include <iostream>
using namespace std;

int main()
{
	int a, b, c, d, e;
	cin >> a >> b >> c >> d;
	e = (a + b + c + d) / 4;
	if (a > e) {
		cout << a << '>' << e << endl;
	}
	else if (a < e) {
		cout << a << '<' << e << endl;
	}
	else {
		cout << a << "==" << e << endl;
	}
	if (b > e) {
		cout << b << '>' << e << endl;
	}
	else if (b < e) {
		cout << b << '<' << e << endl;
	}
	else {
		cout << b << "==" << e << endl;
	}
	if (c > e) {
		cout << c << '>' << e << endl;
	}
	else if (c < e) {
		cout << c << '<' << e << endl;
	}
	else {
		cout << c << "==" << e << endl;
	}
	if (d > e) {
		cout << d << '>' << e << endl;
	}
	else if (e < e) {
		cout << d << '<' << e << endl;
	}
	else {
		cout << d << "==" << e << endl;
	}




	return 0;
}