#include <iostream>
using namespace std;

int arr[3][3] = { 0 };

int main()
{
	int a;
	cin >> a;
	if (a % 5 == 1) {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				arr[x][y] = 9 - x - 3 * y;
			}
		}
	}
	else if (a % 5 == 2) {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				arr[x][y] = 7 + y - 3 * x;
			}
		}
	}
	else {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				arr[x][y] = 10 + x + 3 * y;
			}
		}
	}

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}

	return 0;
}