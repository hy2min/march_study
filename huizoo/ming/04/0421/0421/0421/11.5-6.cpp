#include <iostream>
using namespace std;

char arr[3][3] = {
	{'a','b','E'},
	{'E','2','W'},
	{'3','2','4'}
};

int main()
{
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] >= 'a' && arr[x][y] <= 'z') {
				cout << char(arr[x][y] - 32) << ' ';
			}
			else if (arr[x][y] >= 'A' && arr[x][y] <= 'Z') {
				cout << char(arr[x][y] + 32) << ' ';
			}
			else if (arr[x][y] >= '0' && arr[x][y] <= '9') {
				cout << arr[x][y] - '0' + 5 << ' ';
			}
		}
		cout << endl;
	}



	return 0;
}