#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	int c = a * b;
	if (c <= 30) {
		cout << "작은 사이즈";
	}
	else if (c >= 50) {
		cout << "큰 사이즈";
	}
	else {
		cout << "적당한 사이즈";
	}



	return 0;
}