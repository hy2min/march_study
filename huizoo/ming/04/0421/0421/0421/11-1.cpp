#include <iostream>
using namespace std;

int input();
void calc(int a, int b, int c);

int main()
{
	int a, b, c;
	a = input();
	b = input();
	c = input();
	calc(a, b, c);

	return 0;
}

int input()
{
	int a;
	cin >> a;
	return a;
}

void calc(int a, int b, int c)
{
	cout << a + b + c;
}

