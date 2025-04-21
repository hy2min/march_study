#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	int *p, *t;
	p = &a;
	t = &b;
	int temp = *p;
	*p = *t;
	*t = temp;
	cout << *p << ' '<< *t;


	return 0;
}