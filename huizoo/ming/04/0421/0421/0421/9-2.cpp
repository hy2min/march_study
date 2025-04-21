#include <iostream>
using namespace std;

int main()
{
	char arr[3][5] = { { 'A','B','C','D','E' }, { 'E','A','B','A','B' }, { 'A','C','D','E','R' } };
	char ch;
	cin >> ch;
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 5; y++) {
			if (arr[x][y] == ch) {
				cnt++;
			}
		}
	}
	if (cnt >= 3) {
		cout << "대발견";
	}
	else if (cnt >= 1) {
		cout << "발견";
	}
	else {
		cout << "미발견";
	}



	return 0;
}