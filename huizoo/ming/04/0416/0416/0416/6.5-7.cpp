#include <iostream>
using namespace std;

int main()
{
	char a, b;
	cin >> a >> b;
	if (a >= 'a' && a <= 'z') {
		a = char(a - 'a' + 'A');
	}
	else if (a >= 'A' && a <= 'Z') {
		a = char(a - 'A' + 'a');
	}

	if (b >= 'a' && b <= 'z') {
		b = char(b - 'a' + 'A');
	}
	else if (a >= 'A' && b <= 'Z') {
		b = char(b - 'A' + 'a');
	}

	cout << a << ' ' << b;


	return 0;
}