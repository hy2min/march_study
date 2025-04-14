#include <iostream>
using namespace std;

int main()
{
	int lst[4];
	for (int x = 0; x < 4; x++) {
		cin >> lst[x];
	}
	int Sum = 0;
	for (int x = 0; x < 4; x++) {
		Sum += lst[x];
	}
	cout << Sum;


	return 0;
}