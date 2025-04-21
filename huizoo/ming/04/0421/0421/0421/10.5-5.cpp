#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	int arr[3][4] = { 0 };
	cin >> a >> b >> c;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 4; y++) {
			if (x == 0) {
				arr[x][y] = a;
				a++;
			}
			else if (x == 1) {
				arr[x][y] = b;
				b++;
			}
			else {
				arr[x][y] = c;
				c++;
			}
		}
	}

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 4; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}


	return 0;
}