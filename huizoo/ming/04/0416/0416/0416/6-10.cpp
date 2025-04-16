#include <iostream>
using namespace std;

int main()
{
	char ch;
	cin >> ch;
	if (ch >= 'a' && ch <= 'z') {
		cout << char(ch - 'a' + 'A');
	}
	else if (ch >= 'A'&&ch <= 'Z') {
		cout << char(ch - 'A' + 'a');
	}



	return 0;
}