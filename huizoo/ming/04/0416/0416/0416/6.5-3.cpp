#include <iostream>
using namespace std;


int main()
{
	int arr[5], arr2[5];

	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
		arr2[x] = arr[x];
	}
	for (int x = 0; x < 5; x++) {
		cout << arr[x] << ' ';
	}
	cout << endl;
	for (int x = 0; x < 5; x++) {
		cout << arr2[x] << ' ';
	}

	return 0;
}