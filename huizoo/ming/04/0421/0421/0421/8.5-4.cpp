#include <iostream>
using namespace std;

char arr[17] = { 0 };
char a, b, c;

void input()
{
	cin >> a >> b >> c;
	for (int x = 0; x <= 6; x++) {
		arr[x] = a;
	}
	for (int x = 7; x <= 12; x++) {
		arr[x] = b;
	}
	for (int x = 13; x <= 16; x++) {
		arr[x] = c;
	}

}

int main()
{
	input();
	for (int x = 16; x >= 0; x--) {
		cout << arr[x];
	}

	return 0;
}