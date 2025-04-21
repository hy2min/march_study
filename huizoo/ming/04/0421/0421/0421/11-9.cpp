#include <iostream>
using namespace std;

char arr[8] = { 0 };

int main()
{
	for (int x = 0; x < 8; x++) {
		cin >> arr[x];
	}
	char big[8] = { 0 };
	char small[8] = { 0 };
	int b = 0;
	int s = 0;
	for (int x = 0; x < 8; x++) {
		if (arr[x] >= 'a' & arr[x] <= 'z') {
			small[s] = arr[x];
			s++;
		}
		else {
			big[b] = arr[x];
			b++;
		}
	}
	cout << "big=";
	for (int x = 0; x < b; x++) {
		cout << big[x];
	}
	cout << endl;
	cout << "small=";
	for (int x = 0; x < s; x++) {
		cout << small[x];
	}

	return 0;
}