#include <iostream>
using namespace std;


void CompareGo(int *arr, int *arr2)
{
	for (int x = 0; x < 5; x++) {
		if (arr[x] != arr2[x]) {
			cout << "두배열은같지않음";
			return;
		}
	}

	cout << "두배열은완전같음";


}



int main()
{
	int arr[5] = { 3,5,1,2,7 };
	int arr2[5] = { 0 };
	for (int x = 0; x < 5; x++) {
		cin >> arr2[x];
	}
	CompareGo(arr, arr2);

	return 0;
}

// 13.5-1부터 하면됨