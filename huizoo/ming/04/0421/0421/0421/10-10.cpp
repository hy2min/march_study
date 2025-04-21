#include <iostream>
using namespace std;

int arr[3][4] = { 0 };

int main()
{
	int a;
	cin >> a;

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 4; y++) {
			arr[x][y] = 12 - 4 * x - y;
		}
	}
	for (int x = 0; x < 3; x++) {
		arr[x][a] = 0;
	}

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 4; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}


	return 0;
}