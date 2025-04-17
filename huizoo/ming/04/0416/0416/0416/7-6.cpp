#include <iostream>
using namespace std;

int main()
{
	int a;
	for (int x = 0; x < 4; x++) {

		cin >> a;
		if (a < 20) {
			cout << "더 큰수를 입력하세요";
		}
		else if (a > 20) {
			cout << "더 작은수를 입력하세요";
		}
		else {
			cout << "정답입니다";
		}
		cout << endl;
	}




	return 0;
}