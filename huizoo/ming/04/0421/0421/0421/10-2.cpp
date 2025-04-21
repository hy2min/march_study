#include <iostream>
using namespace std;

int arr[4][4] = { 0 };

int main()
{
	int a;
	cin >> a;
	if (a % 2 == 0) {
		for (int x = 0; x < 4; x++) {
			arr[x][x] = x + 1;
		}
	}
	else {
		for (int x = 0; x < 4; x++) {
			arr[x][3 - x] = x + 1;
		}
	}
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}


	return 0;
}