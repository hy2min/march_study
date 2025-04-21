#include <iostream>
using namespace std;

int arr[2][3] = { 0 };
int Sum = 0;

void input()
{
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			cin >> arr[x][y];
		}
	}

}

void process()
{
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 3; y++) {
			Sum += arr[x][y];
		}
	}
	
}

void output()
{
	cout << Sum;
}

int main()
{
	input();
	process();
	output();


	return 0;
}