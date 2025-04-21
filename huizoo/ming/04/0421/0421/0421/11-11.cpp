#include <iostream>
using namespace std;

int arr[4][4] = {
	{1,3,6,2},
	{4,2,4,5},
	{6,3,7,3},
	{1,5,4,6}
};

int main()
{
	int a;
	cin >> a;
	int select[16] = { 0 };
	int t = 0;
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			if (arr[x][y] > a) {
				select[t] = arr[x][y];
				t++;
			}
		}
	}

	for (int x = 0; x < t; x++) {
		cout << select[x] << ' ';
	}


	return 0;
}