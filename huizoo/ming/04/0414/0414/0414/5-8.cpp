#include <iostream>
using namespace std;

int a;

void KFC()
{
	cin >> a;
}
void BBQ()
{
	if (a > 5) {
		cout << "����";
	}
	else {
		cout << "�ٽ�";
	}
}
int main()
{
	KFC();
	BBQ();

	return 0;
}