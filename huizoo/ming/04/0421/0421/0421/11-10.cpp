#include <iostream>
using namespace std;

int arr[2][5] = {
	{3,2,6,2,4},
	{1,4,2,6,5}
};

int KFC(int target)
{
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 5; y++) {
			if (arr[x][y] == target) {
				return 1;
			}
		}
	}
	return 0;

}

int main()
{
	int target;
	cin >> target;
	int ret = KFC(target);

	if (ret == 1) {
		cout << "���� �����մϴ�";
	}
	else {
		cout << "���� �����ϴ�";
	}


	return 0;
}