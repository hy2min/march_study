#include <iostream>
using namespace std;

void KFC()
{
	for (int x = 0; x < 10; x++) {
		cout << '#';
	}
	cout << endl;
}

void MC()
{
	for (int x = 0; x < 10; x++) {
		cout << '@';
	}
	cout << endl;

}


int main()
{
	KFC();
	MC();
	return 0;
}