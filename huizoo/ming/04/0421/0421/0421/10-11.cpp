#include <iostream>
using namespace std;

int arr[4][4] = { 0 };

int main()
{
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			cin >> arr[x][y];
		}
	}

	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			if (arr[x][y] == 0){
				cout << "!";
			}
			else if (arr[x][y] % 2 == 0) {
				cout << "#";
			}

			else {
				cout << "@";
			}
		}
		cout << endl;
	}



	return 0;
}