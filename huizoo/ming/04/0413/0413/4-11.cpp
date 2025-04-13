#include <iostream>
using namespace std;

int main()
{
	int arr[4];
	for (int x = 0; x < 4; x++) {
		cin >> arr[x];
	}
	int Sum = 0;
	for (int x = 0; x < 4; x++) {
		Sum += arr[x];
	}
	cout << Sum;


	return 0;
}