#include <iostream>
using namespace std;

int arr[6][2] = { 0 };

int main()
{
	int temp;
	int cnt = 0;

	for (int x = 0; x < 6; x++) {
		for (int y = 0; y < 2; y++) {
			cin >> arr[x][y];
		}
		if (arr[x][1] > arr[x][0]) {
			temp = arr[x][0];
			arr[x][0] = arr[x][1];
			arr[x][1] = temp;
			cnt++;
		}
	}

	for (int x = 0; x < 6; x++) {
		for (int y = 0; y < 2; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}

	cout << cnt << "Έν";
	



	return 0;
}