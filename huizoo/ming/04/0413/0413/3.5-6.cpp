#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	int c = a * b;
	if (c <= 30) {
		cout << "���� ������";
	}
	else if (c >= 50) {
		cout << "ū ������";
	}
	else {
		cout << "������ ������";
	}



	return 0;
}