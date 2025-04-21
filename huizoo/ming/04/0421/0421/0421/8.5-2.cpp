#include <iostream>
using namespace std;

int main()
{
	char arr[6] = {'D','T','A','B','W','Q'};
	char t;
	cin >> t;

	for (int x = 0; x < 6; x++) {
		if (arr[x] == t) {
			cout << x << "¹ø INDEX";
		}
	}
	


	return 0;
}