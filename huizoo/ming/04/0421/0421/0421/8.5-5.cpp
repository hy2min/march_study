#include <iostream>
using namespace std;

int main()
{
	char a, b;
	int c;

	cin >> a >> b >> c;

	for (int y = 0; y < c; y++) {
		for (char x = a; x <= b; x++) {
			cout << x;
		}
		cout << endl;
	}


	return 0;
}