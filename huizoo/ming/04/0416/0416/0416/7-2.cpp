#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	if (a >= b) {
		if ((a - b) % 2 == 0) {
			cout << "¦�����";
		}
		else {
			cout << "����Ѵ�";
		}
	}
	else {
		if ((b - a) % 2 == 0) {
			cout << "¦�����";
		}
		else {
			cout << "����Ѵ�";
		}
	}





	return 0;

}