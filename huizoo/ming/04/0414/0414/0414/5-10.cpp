#include <iostream>
using namespace std;

char arr[4];

void input()
{
	for (int x = 0; x < 4; x++) {
		cin >> arr[x];
	}
}

void output()
{
	for (int x = 3; x >= 0; x--) {
		cout << arr[x];
	}

}

int main()
{
	input();
	output();

	return 0;
}