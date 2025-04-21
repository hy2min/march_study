#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	for (int x = 0; x < 6; x++) {
		if (x < 3) {
			for (int y = 0; y < 5; y++) {
				cout << a;
			}
		}
		else {
			for (int y = 0; y < 3; y++) {
				cout << a;
			}
		}
		cout << endl;
	}



	
	return 0;
}