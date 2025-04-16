#include <iostream>
using namespace std;

int main()
{
	char arr[5], arr2[5], t;
	cin >> t;
	for (int x = 0; x < 5; x++) {
		arr[x] = char(t + x);
		cout << arr[x];
	}
	cout << endl;
	for (int x = 0; x < 5; x++) {
		arr2[x] = char(t - x);
		cout << arr2[x];
	}

	

	return 0;
}