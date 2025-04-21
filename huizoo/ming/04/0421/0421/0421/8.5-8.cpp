#include <iostream>
using namespace std;

int main()
{
	int arr[6][3] = { 0 };
	int a, b;
	cin >> a >> b;
	for (int x = 0; x < 6; x++) {
		for (int y = 0; y < 3; y++) {
			if (x < 3) {
				arr[x][y] = a;
			}
			else {
				arr[x][y] = b;
			}
		}
	}
	for (int x = 0; x < 6; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y];
		}
		cout << endl;
	}



	return 0;
}