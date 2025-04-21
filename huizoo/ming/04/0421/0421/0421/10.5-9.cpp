#include <iostream>
using namespace std;

struct BBQ{
	int x;
	int data[3];
};

int main()
{
	BBQ g;
	cin >> g.x;
	for (int t = 0; t < 3; t++) {
		cin >> g.data[t];
	}

	int Sum = 0;
	for (int t = 0; t < 3; t++) {
		Sum += g.data[t];
	}
	cout << Sum << ' ' << g.x;

	return 0;
}