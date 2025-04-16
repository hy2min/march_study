#include <iostream>
using namespace std;

int main()
{
	char arr[5];
	int cnt = 0;

	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
		if (arr[x] >= '0' && arr[x] <= '9') {
			cnt += 1;
		}
	}

	if (cnt > 0) {
		cout << "숫자" << cnt << "개발견";
	}
	else {
		cout << "숫자미발견";
	}


	return 0;
}