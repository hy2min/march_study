#include <iostream>
using namespace std;

void KFC(char *st, int *up, int *low)
{
	for (int x = 0; x < 11; x++) {
		char i = st[x];
		if ( i == '\0') {
			return;
		}
		else if (i >= 'a' && i <= 'z') {
			(*low)++;
		}
		else if (i >= 'A' && i <= 'Z') {
			(*up)++;
		}
	}


}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	char st[11];
	cin >> st;
	int up, low;
	up = 0; low = 0;
	KFC(st, &up, &low);
	cout << "�빮��" << up << "��\n";
	cout << "�ҹ���" << low << "��";

	return 0;
}




// 13-5 ���� ����