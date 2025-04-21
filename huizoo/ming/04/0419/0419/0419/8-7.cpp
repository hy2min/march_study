#include <iostream>
using namespace std;

char arr[5] = { 'B','D','5','Q','A' };
char arr2[5] = { 'Q','E','R','E','F' };
char ch;

void input()
{
	cin >> ch;

}

void output()
{
	if (ch >= 'a' && ch <= 'z') {
		for (int x = 0; x < 5; x++) {
			cout << arr[x];
		}
	}
	else if (ch >= 'A'&&ch <= 'Z') {
		for (int x = 0; x < 5; x++){
			cout << arr2[x];
		}
	}
	else if (ch >= '0'&&ch <= '9') {
		for (char x = 'H'; x >= 'A'; x--) {
			cout << x;
		}
	}

}

int main()
{
	input();
	output();


	return 0;
}