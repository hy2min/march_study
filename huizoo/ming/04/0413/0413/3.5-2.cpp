#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			cout << a;
		}
		cout << endl;
		a++;
	}


	return 0;
}