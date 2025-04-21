#include <iostream>
using namespace std;

int arr[2][3] = { 0 };

int main()
{
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			cin >> arr[x][y];
		}
	}
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] == 0) {
				cout << '#';
			}
			else {
				cout << arr[x][y];
			}
		}
		cout << endl;
	}


	return 0;
}