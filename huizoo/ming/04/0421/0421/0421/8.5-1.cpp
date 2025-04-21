#include <iostream>
using namespace std;

int main()
{
	int arr[6] = { 0 };

	for (int x = 0; x < 6; x++) {
		cin >> arr[x];
		if (arr[x] < 5) {
			cout << x << "번은 " << arr[x] << "점 불합격";
		}
		else {
			cout << x << "번은 " << arr[x] << "점 합격";
		}
		cout << endl;
	}

	
	


	return 0;
}