#include <iostream>
using namespace std;

char arr[3][6] = { 0 };

int main()
{
	char a, b;
	cin >> a >> b;
	for (int y = 0; y < 3; y++) {
		for (int x = 0; x < 6; x++) {
			if (x < 4) {
				arr[y][x] = a;
			}
			else {
				arr[y][x] = b;
			}
		}
	}
	
	for (int y = 0; y < 3; y++) {
		for (int x = 0; x < 6; x++) {
			cout << arr[y][x];
		}
		cout << endl;
	}


	return 0;
}