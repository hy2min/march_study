#include <iostream>
using namespace std;

int arr[3][3] = {
	{3,1,6},
	{7,8,4},
	{9,2,3}
};

int main()
{
	int y, x, a;
	cin >> y >> x >> a;
	arr[y][x] = a;

	int Min = 1e9;
	int Max = -1e9;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (arr[i][j] > Max) {
				Max = arr[i][j];
			}
			if (arr[i][j] < Min) {
				Min = arr[i][j];
			}
		}
	}
	cout << Max + Min;

	return 0;
}