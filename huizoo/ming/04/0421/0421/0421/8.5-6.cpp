#include <iostream>
using namespace std;

int main()
{
	char x;
	int a;
	cin >> x >> a;
	for (int i = 0; i < a; i++) {
		for (int i = 0; i < a; i++) {
			cout << x;
		}
		cout << endl;
	}


	return 0;
}