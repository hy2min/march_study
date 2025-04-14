#include <iostream>
using namespace std;

int main()
{
	int arr[6] = { 0 };
	int a, b;
	cin >> a >> b;
	int c = b - a;
	for (int x = 0; x <= c; x++) {
		arr[x] = a;
		a++;
	}
	
	for (int x = 0; x <= c; x++) {
		cout << arr[x];
	}

	return 0;
}