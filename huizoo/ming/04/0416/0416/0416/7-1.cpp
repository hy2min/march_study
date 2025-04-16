#include <iostream>
using namespace std;

int main()
{
	int arr[5] = { 3,5,2,4,1 };
	int arr2[3][2] = { {9,8},{7,1},{3,4} };

	int a;
	cin >> a;

	if (a % 2 == 0) {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 2; y++) {
				cout << arr2[x][y];
			}
			cout << endl;
		}
	}
	else {
		for (int x = 0; x < 5; x++) {
			cout << arr[x];
		}
	}


	return 0;
}