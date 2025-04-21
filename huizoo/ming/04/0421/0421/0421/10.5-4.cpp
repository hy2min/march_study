#include <iostream>
using namespace std;

char arr[3][5] = {
	{'D','A','C','C','D'},
	{'S','D','F','A','E'},
	{'E','E','T','J','H'}
};

int check(char a)
{
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 5; y++) {
			if (arr[x][y] == a) {
				return 1;
			}
		}
	}
	return 0;
}

void input()
{
	char a;
	cin >> a;
	int ret = check(a);
	if (ret == 1) {
		cout << "있음";
	}
	else {
		cout << "없음";
	}

}


int main()
{
	input();

	return 0;
}