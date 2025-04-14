#include <iostream>
using namespace std;

int main()
{
	int arr[10] = { 5,7,1,8,-4,-73,4,2,20,84 };
	int a;
	cin >> a;
	for (int x = a; x >= 0; x--) {
		cout << arr[x] << endl;
	}



	return 0;
}