#include <iostream>
using namespace std;

int main()
{
	char a, b, c;
	cin >> a >> b >> c;
	char *p1, *p2, *p3;
	p1 = &a;
	p2 = &b;
	p3 = &c;
	*p1 += 1;
	*p2 += 1;
	*p3 += 1;
	cout << *p1 << ' ' << *p2 << ' ' << *p3;

	return 0;
}