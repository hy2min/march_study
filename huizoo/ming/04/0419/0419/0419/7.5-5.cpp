#include <iostream>
using namespace std;

char arr[3] = { 0 };

int main() {
	int cnt = 0;
	for (int x = 0; x < 3; x++) {
		cin >> arr[x];
		if (arr[x] >= 'A' && arr[x] <= 'Z') {
			cnt += 1;
		}
	}
	if (cnt == 3) {
		cout << "ǳ���ϴ�";
	}
	else if (cnt >= 1 && cnt <= 2) {
		cout << "�����ϴ�";
	}
	else if (cnt == 0) {
		cout << "�����ϴ�";
	}

	return 0;
}