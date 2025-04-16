#include <iostream>
using namespace std;

int main()
{
	char arr[3];
	for (int i = 0; i < 3; i++) {
		cin >> arr[i];
	}
	if (arr[0] > arr[1] && arr[0] > arr[2]) {
		cout << "¿Ç´Ù" << arr[0];
	}
	else {
		cout << "¿ÇÁö¾ÊÀ½";
	}

	return 0;
}