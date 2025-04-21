#include <iostream>
using namespace std;

int arr[3][3] = {
{3,5,14},
{2,3,9},
{6,2,7}
};

int main()
{
	int a;
	cin >> a;
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if ((arr[x][y] % a) == 0) {
				cnt += 1;
			}
		}
	}

	cout << cnt;

	return 0;
}