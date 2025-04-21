#include <iostream>
using namespace std;

int main()
{
	char arr[8] = { 4,3,6,1,3,1,5,3 };
	int a;
	cin >> a;
	int cnt = 0;
	for (int x = 0; x < 8; x++) {
		if (arr[x] == a) {
			cnt++;
		}
	}
	cout << "숫자" << a << "개수는" << cnt << "개";

	return 0;
}