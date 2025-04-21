#include <iostream>
using namespace std;

int arr[2][3] = { 0 };

int main()
{
	for (int x = 1; x >= 0; x--) {
		for (int y = 2; y >= 0; y--) {
			cin >> arr[x][y];
		}
	}
	int arr2[6];
	int t = 0;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			arr2[t] = arr[x][y];
			t++;
		}
	}
	int temp = arr2[0];
	arr2[0] = arr2[5];
	arr2[5] = temp;

	for (int x = 0; x < 6; x++) {
		cout << arr2[x] << ' ';
	}


	return 0;
}