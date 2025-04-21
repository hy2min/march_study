#include <iostream>
using namespace std;


int arr[4][4] = { 0 };

int main()
{
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			arr[x][y] = 2 + 2 * x + 8 * y;
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