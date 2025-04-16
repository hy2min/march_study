#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	for (int x = 0; x < c; x++) {
		for (int y=a; y<=b;y++){
			cout << y << ' ';
		}
		cout << endl;
	}



	return 0;
}