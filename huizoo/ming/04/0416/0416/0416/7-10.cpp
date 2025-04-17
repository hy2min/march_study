#include <iostream>
using namespace std;

char arr[4][4];
char ch;

void input()
{
	cin >> ch;
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			arr[x][y] = ch;
		}
	}
	
}

void output()
{

	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			cout << arr[x][y];
		}
		cout << endl;
	}


}

int main()
{
	input();
	output();


	return 0;
}