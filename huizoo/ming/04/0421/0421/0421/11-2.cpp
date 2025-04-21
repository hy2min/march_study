#include <iostream>
using namespace std;

void print(int a)
{
	cout << a;
}


int sum(int a, int b)
{
	return a + b;
}

int comp(int a, int b)
{
	return a - b;
}

int main()
{
	int a, b;
	cin >> a >> b;
	cout << "Че:" << sum(a, b) << endl;
	cout << "Тї:" << comp(a, b);


	return 0;
}