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
			cout << "대문자들";
		}
		else {
			cout << "대소문자";
		}
	}
	else {
		if (b >= 'A'&& b <= 'Z') {
			cout << "대소문자";
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