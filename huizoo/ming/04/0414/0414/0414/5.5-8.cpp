#include <iostream>
using namespace std;

int main()
{
	int arr[6], a, b;
	cin >> a >> b;
	for (int x = 0; x <= 2; x++) {
		arr[x] = a;
		a++;
	}
	for (int x = 5; x >= 3; x--) {
		arr[x] = b;
		b--;
	}

	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}

	return 0;
}