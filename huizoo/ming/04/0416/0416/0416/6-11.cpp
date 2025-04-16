#include <iostream>
using namespace std;

int main()
{
	char ch1, ch2;
	cin >> ch1 >> ch2;
	for (int i = 0; i < 4; i++) {
		for (char x = ch1; x <= ch2; x++) {
			cout << x << ' ';
		}
		cout << endl;
	}


	return 0;
}