#include <iostream>
using namespace std;

int main()
{
	char arr[4] = { 'B','T','K','A' };
	int a;
	cin >> a;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < 4; j++) {
			cout << arr[j] << ' ';
		}
		cout << endl;
	}



	return 0;
}