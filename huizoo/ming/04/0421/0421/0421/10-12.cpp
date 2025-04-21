#include <iostream>
using namespace std;

int INPUT()
{
	int a;
	cin >> a;
	return a;
}

void CountDown(int a)
{
	for (int x = a; x >= 1; x--) {
		cout << x << ' ';
	}

}

int main()
{
	int a = INPUT();
	CountDown(a);

	return 0;
}