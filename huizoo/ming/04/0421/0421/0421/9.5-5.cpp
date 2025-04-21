#include <iostream>
using namespace std;

char arr[2][3] = { 0 };

void input()
{
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			cin >> arr[x][y];
		}
	}

}

void findUpper()
{
	int cnt = 0;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] >= 'A' && arr[x][y] <= 'Z') {
				++cnt;
			}
		}
	}
	cout << "대문자" << cnt << "개" << endl;
}

void findLower()
{
	int cnt = 0;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] >= 'a' && arr[x][y] <= 'z') {
				++cnt;
			}
		}
	}
	cout << "소문자" << cnt << "개" << endl;

}

int main()
{
	input();
	findUpper();
	findLower();


	return 0;
}