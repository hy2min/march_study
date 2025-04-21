#include <iostream>
using namespace std;

int a, b;

void input()
{
	cin >> a >> b;


}

void output()
{
	int Sum = a + b;
	int i = 5;
	while (i <= Sum) {
		cout << i << ' ';
		i++;
	}

}


int main()
{
	input();
	output();


	return 0;
}