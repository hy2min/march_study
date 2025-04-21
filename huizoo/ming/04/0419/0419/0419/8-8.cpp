#include <iostream>
using namespace std;

char arr[6] = { '#', '_','#','_','#', '#' };

int main()
{
	for (int x = 0; x < 6; x++) {
		if (arr[x] == '#') {
			cout << "¼¥";
		}
		else if (arr[x] == '_') {
			cout << "¹«";
		}
	}

	return 0;

}