#include <iostream>
using namespace std;


int one() {
	int a;
	cin >> a;
	return a;
}

char two() {
	char a;
	cin >> a;
	return a;
}

int main()
{
	cout << one();
	cout << two();
	return 0;
}