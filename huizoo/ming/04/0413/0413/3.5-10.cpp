#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	int b = 1;
	for (int x = 0; x < a; x++) {
		cout << b << ' ';
		b += 2;
	}



	return 0;
}