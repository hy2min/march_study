#include <iostream>
using namespace std;

int main()
{
	char st[100];
	cin >> st;
	char last;
	int n;
	for (int x = 0; x < 100; x++) {
		if (st[x] == '\0') {
			last = st[x-1];
			n = x;
			break;
		}
	}
	int cnt = 0;
	for (int x = 0; x < n; x++) {
		if (st[x] == last) {
			cnt += 1;
		}
	}
	cout << n << endl << cnt;




	return 0;
}

// 12.5�� 6�� Ǯ������ 12.4, 12.5�� ���� ��Ǯ���� Ǯ�����