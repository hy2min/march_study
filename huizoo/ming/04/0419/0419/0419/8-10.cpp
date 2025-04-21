#include <iostream>
using namespace std;

int arr[3][4] = { { 4,3,1,1 }, { 3,1,2,1 }, { 0,0,1,2 } };

int main()
{
	int a, cnt;
	cin >> a;
	cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 4; y++) {
			if (arr[x][y] == a) {
				cnt += 1;
			}
		}
	}

	cout << cnt << "개 존재합니다";



	return 0;
}