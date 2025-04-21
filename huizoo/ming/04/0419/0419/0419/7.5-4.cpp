#include <iostream>
using namespace std;

char arr[3][5] = { 0 };

int main() {
	char a;
	cin >> a;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 5; y++) {
			arr[x][y] = a++;
		}
	}

	cout << char(arr[2][2]+32);

	return 0;
}