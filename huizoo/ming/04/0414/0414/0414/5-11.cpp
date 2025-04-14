#include <iostream>
using namespace std;

int arr[6];

void PrintAll()
{
	for (int x = 0; x < 6; x++) {
		cout << arr[x] << endl;
	}
}

int main()
{
	int a;
	cin >> a;
	for (int x = 0; x < 6; x++) {
		arr[x] = a;
		a++;
	}

	PrintAll();

	return 0;
}