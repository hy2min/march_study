#include <iostream>
using namespace std;

int main()
{
	int arr[3][3] = { {3,4,1},{2,1,4},{3,3,0} };
	int odd = 0;
	int even = 0;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] % 2 == 0) {
				even += 1;
			}
			else {
				odd += 1;
			}
		}
	}

	cout << "¦�� : " << even << endl;
	cout << "Ȧ�� : " << odd;

	return 0;
}