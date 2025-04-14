#include <iostream>
using namespace std;

int main()
{
	int arr[5];
	int Sum = 0;
	for (int x = 0; x < 5; x++) {
		cin >> arr[x];
		Sum += arr[x];
	}
	cout << "합은 " << Sum << "입니다";



	return 0;
}