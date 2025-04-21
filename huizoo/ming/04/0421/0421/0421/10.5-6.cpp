#include <iostream>
using namespace std;

int arr[6][3] = {
	{10,16,22},
	{11,17,23},
	{12,18,24},
	{13,19,25},
	{14,20,26},
	{15,21,27}
};

int main()
{
	int a, b;
	cin >> a >> b;
	for (int x = a; x <= b; x++) {
		for (int y = 0; y < 3; y++) {
			arr[x][y] = 7;
		}
	}

	for (int x = 0; x < 6; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y] << ' ';
		}
		cout << endl;
	}


	return 0;
}