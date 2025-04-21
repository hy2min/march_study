#include <iostream>
using namespace std;

int arr[7] = { 0 };

int main()
{
	int Min = 1e9;
	int Max = -1e9;
	for (int x = 0; x < 7; x++) {
		cin >> arr[x];
		if (arr[x] < Min) {
			Min = arr[x];
		}
		if (arr[x] > Max) {
			Max = arr[x];
		}
	}
	cout << "MAX=" << Max << endl;
	cout << "MIN=" << Min;



	return 0;
}