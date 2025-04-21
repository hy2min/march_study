#include <iostream>
using namespace std;

char arr[3][5] = {
	{'a','b','a','c','z'},
	{'c','t','a','c','d'},
	{'c','c','c','c','a'}
};

int main()
{
	char a;
	cin >> a;
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 5; y++) {
			if (arr[x][y] == a) {
				cnt += 1;
			}
		}
	}
	if (cnt >= 7) {
		cout << "세상에";
	}
	else if (cnt >= 5) {
		cout << "와우";
	}
	else if (cnt >= 3) {
		cout << "이야";
	}
	else {
		cout << "이런";
	}



	return 0;
}