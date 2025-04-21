#include <iostream>
using namespace std;

char arr[3][3] = { 0 };

int main()
{
	char t = 'A';
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			arr[i][j] = t;
			t++;
		}
	}

	int y1, x1, y2, x2;
	cin >> y1 >> x1 >> y2 >> x2;
	int temp = arr[y1][x1];
	arr[y1][x1] = arr[y2][x2];
	arr[y2][x2] = temp;


	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cout << arr[i][j];
		}
		cout << endl;
	}



	return 0;
}