#include <iostream>
using namespace std;

int arr[7] = { 3,4,1,3,2,7,3 };

int main()
{
	int a;
	cin >> a;
	int flag = 0;
	for (int x = 0; x < 7; x++) {
		if (arr[x] == a) {
			flag = 1;
		}
	}
	if (flag) {
		cout << "발견";
	}
	else {
		cout << "미발견";
	}


	return 0;
}