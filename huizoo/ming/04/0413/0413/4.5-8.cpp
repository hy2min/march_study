#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	int arr[6];
	for (int x = 0; x < 6; x++) {
		arr[x] = a;
		cout << arr[x] << endl;
		a++;
	}
	



	return 0;
}