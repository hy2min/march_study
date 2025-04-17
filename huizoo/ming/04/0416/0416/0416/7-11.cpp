#include <iostream>
using namespace std;

int a, arr[3][3];

void input()
{
	cin >> a;



}

void process()
{
	int x = a;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			arr[i][j] = x;
			x++;
		}
	}



}

void output()
{
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}



}
int main()
{
	input();
	process();
	output();


	return 0;
}