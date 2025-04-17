#include <iostream>
using namespace std;

int main()
{
	int arr[2][3] = { {3,1,1},{2,3,2} };
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			cout << arr[x][y];
		}
	}




	return 0;
}