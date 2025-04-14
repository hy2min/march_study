#include <iostream>
using namespace std;

int main()
{
	int arr[6], a;
	for (int x = 0; x < 3; x++) {
		cin >> arr[x];
	}
	cin >> a;
	for (int x = 3; x <= 5; x++) {
		arr[x] = a;
		a++;
	}

	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}


	return 0;
}