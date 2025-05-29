#include <iostream>
using namespace std;

int arr[4][4] = {
	{3,4,1,6},
	{3,5,3,6},
	{0},
	{5,4,6,0}
};

int main()
{
	int Min = 1e9;
	int Max = -1e9;
	int y1, y2, x1, x2;


	for (int x = 0; x < 4; x++) {
		cin >> arr[2][x];
	}
	for (int y = 0; y < 4; y++) {
		for (int x = 0; x < 4; x++) {
			if (Min > arr[y][x]) {
				Min = arr[y][x];
				y1 = y; x1 = x;
			}
			if (Max < arr[y][x]) {
				Max = arr[y][x];
				y2 = y; x2 = x;
			}
		}
	}
	cout << "MAX=" << Max << "(" << y2 << "," << x2 << ')' << endl;
	cout << "MIN=" << Min << "(" << y1 << "," << x1 << ')';

	return 0;
}