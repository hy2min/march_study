#include <iostream>
using namespace std;

int main()
{
	int arr[5];
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
		cout << x + 1 << "�������" << arr[x] << "��";
		if (arr[x] >= 70) {
			cout << "PASS";
		}
		else if (arr[x] >= 50) {
			cout << "RETEST";
		}
		else {
			cout << "FAIL";
		}
		cout << endl;
	}


	return 0;
}