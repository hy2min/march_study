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
		cout << "풍족하다";
	}
	else if (cnt >= 1 && cnt <= 2) {
		cout << "적절하다";
	}
	else if (cnt == 0) {
		cout << "부족하다";
	}

	return 0;
}