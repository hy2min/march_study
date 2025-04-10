#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	if ((a + b + c) >= (a*b*c)) {
		cout << "青款狼 荐";
	}
	else {
		cout << "家家茄 荐";
	}
	return 0;
}