#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	a += 5;

	int arr[5];
	for (int x = 0; x < 5; x++) {
		arr[x] = a;
	}

	for (int x = 0; x < 5; x++) {
		cout << arr[x] << ' ';
	}


	return 0;
}