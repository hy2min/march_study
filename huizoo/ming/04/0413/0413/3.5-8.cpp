#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	for (int x = a; x <= b; x++) {
		cout << x << ' ';
	}
	cout << endl;
	for (int x = a; x <= c; x++) {
		cout << x << ' ';
	}



	return 0;
}