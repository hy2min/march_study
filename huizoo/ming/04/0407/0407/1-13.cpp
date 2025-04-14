#include <iostream>
using namespace std;

int main()
{
	int a;
	a = 8;
	cout << a << "\n";
	a = a + 1;
	a++;
	a = 3;
	a = a + 1;
	a++;

	//endl 와 "\n" 로 엔터를 출력할 수 있습니다.
	cout << "a값은 : " << a << endl;

	a = a + 1;
	a++;
	cout << "마지막 a값은 : " << a << endl;
	return 0;
}