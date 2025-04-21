#include <iostream>
using namespace std;

int main()
{
	int arr[3][3] = { 0 };
	int y, x, a;
	cin >> y >> x >> a;
	arr[y][x] = a;

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}

	return 0;
}