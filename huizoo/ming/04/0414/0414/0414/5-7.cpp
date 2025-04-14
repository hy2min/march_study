#include <iostream>
using namespace std;

int main()
{
	int arr[6];
	for (int x = 0; x < 3; x++) {
		cin >> arr[x];
	}
	int a;
	cin >> a;
	for (int x = 0; x < 3; x++) {
		arr[x + 3] = a;
		a++;
	}

	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}

	return 0;
}