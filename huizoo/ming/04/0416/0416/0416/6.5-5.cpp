#include <iostream>
using namespace std;

int main()
{
	int arr[3];
	for (int x = 0; x < 3; x++) {
		cin >> arr[x];
	}
	for (int x = 0; x < (arr[0] + arr[1] + arr[2]); x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[y] << ' ';
		}
		cout << endl;
	}

	return 0;
}