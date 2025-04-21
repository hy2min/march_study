#include <iostream>
using namespace std;

int arr[5][5] = { 0 };

int main()
{
	for (int x = 0; x < 5; x++) {
		for (int y = 0; y < 5; y++) {
			arr[x][y] = 21 + x - 5 * y;
		}
	}
	int a;
	cin >> a;
	for (int x = 0; x < 5; x++) {
		arr[a][x] = a;
	}

	for (int x = 0; x < 5; x++) {
		for (int y = 0; y < 5; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}


	return 0;
}