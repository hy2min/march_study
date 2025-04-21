#include <iostream>
using namespace std;

int main()
{
	int arr[6];
	for (int i = 0; i < 6; i++) {
		cin >> arr[i];
	}

	int a = 0;

	while (a < 6) {
		if (arr[a] == 7) {
			break;
		}
		cout << arr[a] << ' ';

		a++;
	}




	return 0;
}