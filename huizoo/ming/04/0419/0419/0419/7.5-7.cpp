#include <iostream>
using namespace std;


int main()
{
	int arr[3][2] = { 0 };
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 2; y++) {
			cin >> arr[x][y];
			arr[x][y] += 2;
		}
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}


	return 0;
}