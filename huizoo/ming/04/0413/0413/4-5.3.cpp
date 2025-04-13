#include <iostream>
using namespace std;

int main()
{
	int arr[5];
	int a;
	cin >> a;
	for (int x = 0; x < 5; x++) {
		arr[x] = a;
	}

	for (int x = 0; x < 5; x++) {
		cout << arr[x];
	}



	return 0;
}