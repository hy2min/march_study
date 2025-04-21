#include <iostream>
using namespace std;

char arr[5][3] = {
	{'D','A','A'},
	{'B','C','D'},
	{'E','F','A'},
	{'A','A','D'},
	{'F','G','E'},
};


int main()
{
	char a;
	cin >> a;
	for (int y = 0; y < 5; y++) {
		for (int x = 0; x < 3; x++) {
			if (arr[y][x] == a) {
				cout << '(' << y << ',' << x << ')' << endl;
			}
		}
	}


	return 0;
}