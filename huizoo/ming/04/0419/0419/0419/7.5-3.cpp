#include <iostream>
using namespace std;

char a, b;

void input()
{
	cin >> a >> b;
	   
}

void output()
{

	if (a >= 'A' && a <= 'Z') {
		if (b >= 'A'&& b<= 'Z') {
			cout << "�빮�ڵ�";
		}
		else {
			cout << "��ҹ���";
		}
	}
	else {
		if (b >= 'A'&& b <= 'Z') {
			cout << "��ҹ���";
		}
		else {
			for (char x = 'a'; x <= 'z'; x++) {
				cout << x;
			}
		}
	}

}

int main()
{
	input();
	output();


	return 0;
}