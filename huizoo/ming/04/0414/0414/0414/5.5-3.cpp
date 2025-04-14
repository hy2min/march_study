#include <iostream>
using namespace std;

int arr[5];
int arr1[5];

void PrintAll()
{
	for (int x = 0; x < 5; x++) {
		cout << arr[x];
	}
	cout << endl;
	for (int x = 0; x < 5; x++){
		cout << arr1[x];
	}
}


int main()
{
	
	int a, b;
	cin >> a >> b;
	for (int x = 0; x < 5; x++) {
		arr[x] = a;
	}
	for (int x = 0.; x < 5; x++) {
		arr1[x] = b;
	}

	PrintAll();

	return 0;
}