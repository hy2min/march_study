#include <iostream>
using namespace std;


void run(int a)
{
	int arr[3][3] = { 0 };
	if (a < 10) {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				arr[x][y] = 1 + 3 * x + y;
			}
		}
	}
	else {
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				arr[x][y] = 3 + 3 * x - y;
			}
		}
	}

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y];
		}
		cout << endl;
	}
}

int main()
{
	int a;
	cin >> a;
	run(a);


	return 0;
}