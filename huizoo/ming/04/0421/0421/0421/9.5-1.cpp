#include <iostream>
using namespace std;

int A[5] = { 2,1,2,4,5 };
int B[3][3] = { {2,5,3},{4,5,7},{8,7,2} };



int main()
{
	int a;
	cin >> a;
	int cnt1, cnt2;
	cnt1 = 0; cnt2 = 0;

	for (int x = 0; x < 5; x++) {
		if (A[x] == a) {
			cnt1++;
		}
	}

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			if (B[x][y] == a) {
				cnt2++;
			}
		}
	}

	cout << cnt1 + cnt2;


	return 0;
}