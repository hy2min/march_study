#include <iostream>
using namespace std;

char arr[6] = { 'D','F','G','D','A','Q' };

int main()
{
	char ch1, ch2;
	cin >> ch1 >> ch2;
	int flag = 0;
	for (int x = 0; x < 6; x++) {
		if (arr[x] >= ch1 && arr[x] <= ch2) {
			flag = 1;
		}
	}
	if (flag == 1) {
		cout << "발견!!!";
	}
	else {
		cout << "미발견!!!";
	}

	return 0;
}