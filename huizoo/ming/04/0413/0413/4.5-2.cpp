#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;

	if (a != 3) {
		cout << "3�� �ƴϴ�\n";
	}
	if (a != 5) {
		cout << "5�� �ƴϴ�\n";
	}
	if (a >= 1 && a < 10) {
		for (int x = 5; x > 0; x--) {
			cout << x << endl;
		}
	}



	return 0;
}