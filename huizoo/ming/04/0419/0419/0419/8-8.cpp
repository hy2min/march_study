#include <iostream>
using namespace std;

char arr[6] = { '#', '_','#','_','#', '#' };

int main()
{
	for (int x = 0; x < 6; x++) {
		if (arr[x] == '#') {
			cout << "��";
		}
		else if (arr[x] == '_') {
			cout << "��";
		}
	}

	return 0;

}