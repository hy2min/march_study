#include <iostream>
using namespace std;


void CompareGo(int *arr, int *arr2)
{
	for (int x = 0; x < 5; x++) {
		if (arr[x] != arr2[x]) {
			cout << "�ι迭����������";
			return;
		}
	}

	cout << "�ι迭����������";


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

// 13.5-1���� �ϸ��