#include <iostream>
using namespace std;

int arr[5], a;

void KFC()
{
	for (int x = 0; x < 5; x++) {
		cout << arr[x];
	}
}


int main()
{
		cin >> a;
	for (int x = 0; x < 5; x++) {
		arr[x] = a;
		a--;
	}
	KFC();

	return 0;
}