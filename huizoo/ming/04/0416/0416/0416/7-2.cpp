#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	if (a >= b) {
		if ((a - b) % 2 == 0) {
			cout << "Â¦»ç¶û¸¸";
		}
		else {
			cout << "°í¹éÇÑ´Ù";
		}
	}
	else {
		if ((b - a) % 2 == 0) {
			cout << "Â¦»ç¶û¸¸";
		}
		else {
			cout << "°í¹éÇÑ´Ù";
		}
	}





	return 0;

}