#include <iostream>
using namespace std;

int main()
{
	int arr[6] = { 0 };

	for (int x = 0; x < 6; x++) {
		cin >> arr[x];
		if (arr[x] < 5) {
			cout << x << "���� " << arr[x] << "�� ���հ�";
		}
		else {
			cout << x << "���� " << arr[x] << "�� �հ�";
		}
		cout << endl;
	}

	
	


	return 0;
}