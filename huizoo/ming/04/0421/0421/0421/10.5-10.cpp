#include <iostream>
using namespace std;

int arr[7][5] = {
	{1, 0, 0, 0, 0},
	{1, 0, 1, 0, 0},
	{1, 1, 0, 1, 0},
	{1, 0, 1, 0, 0},
	{0, 1, 0, 0, 1},
	{1, 0, 0, 1, 0},
	{1, 1, 0, 0, 0},
};

int input()
{
	int a;
	cin >> a;
	return a;
}

int process(int a)
{
	int cnt = 0;
	for (int x = 0; x < 7; x++) {
		if (arr[x][a] == 1) {
			cnt++;
		}
	}

	return cnt;
}

void output(int a)
{
	cout << a;
}

int main()
{
	
	output(process(input()));

	return 0;
}