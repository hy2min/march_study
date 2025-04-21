#include <iostream>
using namespace std;

int arr[6] = { 0 };

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	arr[a] = 1;
	arr[b] = 1;
	arr[c] = 1;
	
	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}

	return 0;
}