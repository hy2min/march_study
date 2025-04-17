#include <iostream>
using namespace std;

int main()
{
	int arr[5];
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
	}
	int cnt = 0;
	for (int x = 0; x < 5; x++) {
		if (arr[x] >= 3 && arr[x] <= 7) {
			cnt += 1;
		}
	}
	cout << cnt;

	return 0;
}