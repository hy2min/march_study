#include <iostream>
using namespace std;

void BBQ(int a, int b) {
	
	cout << "��:" << a + b << endl;
	cout << "��:" << a - b << endl;
	cout << "��:" << a * b << endl;
	cout << "��:" << a / b << endl;

}


int main()
{
	int a, b;
	cin >> a >> b;
	BBQ(a, b);



	return 0;
}