#include <iostream>
using namespace std;

int main()
{
	int a;
	a = 8;
	cout << a << "\n";
	a = a + 1;
	a++;
	a = 3;
	a = a + 1;
	a++;

	//endl �� "\n" �� ���͸� ����� �� �ֽ��ϴ�.
	cout << "a���� : " << a << endl;

	a = a + 1;
	a++;
	cout << "������ a���� : " << a << endl;
	return 0;
}