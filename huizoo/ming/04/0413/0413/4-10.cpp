#include <iostream>
using namespace std;

int main()
{
	int arr[6];
	int a;
	cin >> a;
	for (int x = 0; x <= 5; x++) {
		arr[x] = a - x;
	}
	cout << arr[2];




	return 0;
}