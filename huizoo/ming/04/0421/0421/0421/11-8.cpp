#include <iostream>
using namespace std;

char arr[13] = { 'S','t','r','u','c','t','P','o','i','n','t','e','r' };

int main()
{
	char a;
	cin >> a;
	int flag = 0;
	for (int x = 0; x < 13; x++) {
		if (arr[x] == a) {
			flag = 1;
		}
	}
	if (flag) {
		cout << "�߰�";
	}
	else {
		cout << "�̹߰�";
	}


	return 0;
}