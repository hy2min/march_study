#include <iostream>
using namespace std;

int main()
{
	int a;
	for (int x = 0; x < 4; x++) {

		cin >> a;
		if (a < 20) {
			cout << "�� ū���� �Է��ϼ���";
		}
		else if (a > 20) {
			cout << "�� �������� �Է��ϼ���";
		}
		else {
			cout << "�����Դϴ�";
		}
		cout << endl;
	}




	return 0;
}