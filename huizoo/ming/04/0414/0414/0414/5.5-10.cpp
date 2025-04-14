#include <iostream>
using namespace std;

int main()
{
	int a, arr[6];
	cin >> a;
	for (int x = 0; x < 6; x++) {
		arr[x] = a + a*x;
	}

	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}

	return 0;
}