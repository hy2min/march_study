#include <iostream>
using namespace std;

int main()
{
	char arr[6] = { 'A','F','G','A','B','C' };
	char a, b;
	cin >> a >> b;
	int aa, bb;
	aa = 0;
	bb = 0;
	for (int x = 0; x < 6; x++) {
		if (arr[x] == a){
			aa++;
		}
		else if (arr[x] == b) {
			bb++;
		}
	}

	if (aa > 0 && bb > 0) {
		cout << "��2��";
	}
	else if (aa >> 0 || bb > 0) {
		cout << "��1��";
	}
	else {
		cout << "��0��";
	}


	return 0;
}