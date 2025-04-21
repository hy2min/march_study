#include <iostream>
using namespace std;


int arr[3][3] = {
	{10,3,20},
	{60,30,40},
	{20,30,40}
};

int main()
{
	int a, b;
	cin >> a >> b;
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] >= a && arr[x][y] <= b) {
				++cnt;
			}
		}
	}

	cout << cnt;



	return 0;
}