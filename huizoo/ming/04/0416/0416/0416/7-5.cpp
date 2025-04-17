#include <iostream>
using namespace std;


int main()
{
	int a;
	cin >> a;
	if (a >= 80) {
		cout << "수";
	}
	else if (a >= 70) {
		cout << "우";
	}
	else if (a >= 60) {
		cout << "미";
	}
	else {
		cout << "재시도";
	}


	return 0;
}