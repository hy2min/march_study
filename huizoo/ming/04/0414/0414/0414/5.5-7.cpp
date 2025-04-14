#include <iostream>
using namespace std;

int main()
{
	int data[4], a;
	cin >> a;
	for (int x = 0; x < 4; x++) {
		data[x] = a;
		a--;
	}

	for (int x = 0; x < 4; x++) {
		cout << data[x] << ' ';
	}


	return 0;
}