#include <iostream>
using namespace std;

int main()
{
	int arr[11] = { 3,4,1,5,8,1,7,7,3,6,9 };
	int a;
	cin >> a;
	for (int x = 0; x < 11; x+=a) {
		cout << arr[x] << ' ';
	}





	return 0;
}