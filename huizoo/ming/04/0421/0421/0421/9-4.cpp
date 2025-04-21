#include <iostream>
using namespace std;

int arr[6] = { 3,4,2,5,7,9 };


int main()
{
	int a, b;
	cin >> a >> b;
	int temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;

	for (int x = 0; x < 6; x++) {
		cout << arr[x] << ' ';
	}


	return 0;
}