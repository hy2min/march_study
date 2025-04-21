#include <iostream>
using namespace std;

char arr[3][3] = {
	{'a','b','d'},
	{'e','w','z'},
	{'q','v','a'}
};

void Process(char a)
{
	a += 32;
	int flag = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] == a) {
				flag = 1;
			}
		}
	}
	if (flag == 1) {
		cout << "존재";
	}
	else {
		cout << "없음";
	}

}

void input()
{
	char a;
	cin >> a;
	Process(a);
}



int main()
{
	input();


	return 0;
}