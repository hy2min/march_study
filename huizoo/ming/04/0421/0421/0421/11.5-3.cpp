#include <iostream>
using namespace std;

char arr[8] = { 'A','1','1','1','5','A','w','z' };

int main()
{
	char a;
	cin >> a;
	int cnt = 0;
	for (int x = 0; x < 8; x++) {
		if (arr[x] == a) {
			cnt++;
		}
	}
	if (cnt >= 3) {
		cout << "THREE";
	}
	else if (cnt == 2) {
		cout << "TWO";
	}
	else if (cnt == 1) {
		cout << "ONE";
	}
	else {
		cout << "NOTHING";
	}


	return 0;
}