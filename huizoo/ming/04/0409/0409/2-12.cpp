#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	if ((a + b + c) >= (a*b*c)) {
		cout << "����� ��";
	}
	else {
		cout << "�Ҽ��� ��";
	}
	return 0;
}