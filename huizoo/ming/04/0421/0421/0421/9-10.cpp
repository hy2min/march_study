#include <iostream>
using namespace std;

char arr[5] = { 0 };


void checkChar(char t) {
	if (t >= 'a'&& t <= 'z') {
		cout << "��";
	}
	else if (t >= 'A'&& t <= 'Z') {
		cout << "��";
	}
}



int main()
{
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
	}

	for (int x = 0; x < 5; x++) {
		checkChar(arr[x]);
	}


	return 0;
}