#include <iostream>
using namespace std;

int main()
{
	int arr[6] = { 0 };
	for (int x = 0; x < 6; x++) {
		cin >> arr[x];
	}
	for (int x = 5; x >= 0; x--) {
		cout << arr[x]<<' ';
		if (arr[x] == 7) {
			break;
		}
	}


	return 0;
}