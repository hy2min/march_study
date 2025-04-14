#include <iostream>
using namespace std;

int main()
{

	int arr[5];
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
	}

	for (int x = 0; x < 5; x++) {
		cout << arr[x] << ' ';
	}

	return 0;
}