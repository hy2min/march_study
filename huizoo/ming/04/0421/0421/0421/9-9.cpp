#include <iostream>
using namespace std;

char arr[2][3] = { {'F','E','W'},{'D','C','A'} };


void findCh(char target) {
	bool found = false;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			if (arr[x][y] == target) {
				found = true;
			}
		}
	}
	if (found == true) {
		cout << "발견";
	}
	else {
		cout << "미발견";
	}

}

int main()
{	
	char ch;
	cin >> ch;
	findCh(ch);

	return 0;
}