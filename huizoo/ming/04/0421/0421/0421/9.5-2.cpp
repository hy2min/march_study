#include <iostream>
using namespace std;

char arr[5] = { 0 };



int main()
{
	int cnt = 0;
	int arr2[5] = { 0 };
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
		if (arr[x] == 'A') {
			cnt++;
			arr2[x] = 1;
		}
	}

	cout << "����A�� " << cnt << "���߰�" << endl;
	for (int x = 0; x < 5; x++) {
		if (arr2[x] == 1) {
			cout << x << "��" << endl;
		}
	}


	return 0;
}