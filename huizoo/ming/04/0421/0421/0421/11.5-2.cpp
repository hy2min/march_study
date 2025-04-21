#include <iostream>
using namespace std;

int arr[3][3] = {
	{1,1,1},
	{1,2,1},
	{3,6,3}
};

int Count(int a)
{
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] == a) {
				cnt++;
			}
		}
	}
	return cnt;
}

int main()
{
	int a;
	cin >> a;
	cout << Count(a);


	return 0;
}