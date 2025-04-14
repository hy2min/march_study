#include <iostream>
using namespace std;

void LOT()
{
	for (int x = 1; x <= 5; x++) {
		cout << x;
	}
	cout << endl;
}

int main()
{
	int a;
	cin >> a;
	
	for (int x = 0; x < a; x++) {
		LOT();
	}


	return 0;
}