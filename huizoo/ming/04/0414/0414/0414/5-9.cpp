#include <iostream>
using namespace std;

char arr[3] = { 'A','B','C' };

void KFC()
{
	for (int x = 0; x < 3; x++) {
		cout << arr[x];
	}
	cout << endl;
}

int main()
{
	int a;
	cin >> a;
	for (int x = 0; x < a; x++) {
		KFC();
	}
	return 0;

}