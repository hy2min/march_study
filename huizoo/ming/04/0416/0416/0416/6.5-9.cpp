#include <iostream>
using namespace std;

int main()
{
	int arr[6] = { 5,4,1,2,7,8 };
	int a;
	cin >> a;
	for (int x = 0; x < a; x++) {
		for (int y = 5; y >=0; y--) {
			cout << arr[y] << ' ';
		}
		cout << endl;
	}



	return 0;
}