#include <iostream>
using namespace std;


int main()
{
	char a;
	cin >> a;
	if (a >= 'a' && a <= 'z') {
		cout << "�ҹ����Է�!!";
	}
	else if (a >= 'A' && a <= 'Z') {
		cout << "�빮���Է�!!";
	}
	else if (a >= '0' && a <= '9') {
		cout << "���ڹ����Է�!!";
	}



	return 0;
}