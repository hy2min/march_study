#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	if (a > b) {
		cout << "큰수는 " << a;
	}
	else if (b > a) {
		cout << "큰수는 " << b;
	}
	else {
		cout << "같은숫자";
	}



	return 0;

}