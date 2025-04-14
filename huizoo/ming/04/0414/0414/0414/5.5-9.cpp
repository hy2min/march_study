#include <iostream>
using namespace std;

int main()
{

	int arr[5], a, b;
	cin >> a >> b;
	for (int x = 0; x < 5; x++) {
		arr[x] = a;
		a += b;
	}

	for (int x = 0; x < 5; x++) {
		cout << arr[x] << ' ';
	}


	return 0;
}