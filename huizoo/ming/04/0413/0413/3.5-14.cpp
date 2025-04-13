#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	if (a == 1111) {
		if (b == 2222) {
			cout << "로그인성공";
		}
		else {
			cout << "비밀번호가 틀렸습니다";
		}
	}
	else {
		cout << "아이디가 틀렸습니다";
	}


	return 0;
}