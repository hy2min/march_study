#include <iostream>
using namespace std;

void QTR()
{
	cout << "QTR100%";
}
void BBQ()
{
	cout << "BBQ100%";
}

int arr[3];

int main()
{
	for (int x = 0; x < 3; x++) {
		cin >> arr[x];
	}
	int Sum = 0;
	for (int x = 0; x < 3; x++) {
		Sum += arr[x];
	}
	if (Sum >= 10) {
		QTR();
	}
	else {
		BBQ();
	}

	return 0;
}