#include <iostream>
using namespace std;

void BBQ(int a, int b) {
	
	cout << "ÇÕ:" << a + b << endl;
	cout << "Â÷:" << a - b << endl;
	cout << "°ö:" << a * b << endl;
	cout << "¸ò:" << a / b << endl;

}


int main()
{
	int a, b;
	cin >> a >> b;
	BBQ(a, b);



	return 0;
}