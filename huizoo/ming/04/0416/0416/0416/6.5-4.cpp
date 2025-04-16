#include <iostream>
using namespace std;


int main()
{
	char a;
	cin >> a;
	if (a >= 'a' && a <= 'z') {
		cout << "소문자입력!!";
	}
	else if (a >= 'A' && a <= 'Z') {
		cout << "대문자입력!!";
	}
	else if (a >= '0' && a <= '9') {
		cout << "숫자문자입력!!";
	}



	return 0;
}