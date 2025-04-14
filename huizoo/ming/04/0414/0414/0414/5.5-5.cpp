#include <iostream>
using namespace std;

int main()
{
	int arr[5] = { 4,1,2,3,5 };
	char st;
	cin >> st;
	if (st == 'a' || st == 'b' || st == 'c') {
		for (int x = 3; x >= 0; x--) {
			cout << arr[x] << ' ';
		}
	}
	else {
		for (int x = 4; x >= 1; x--) {
			cout << arr[x] << ' ';
		}
	}
	return 0;
}