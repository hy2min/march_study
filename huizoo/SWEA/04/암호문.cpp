#include <iostream>
#include <string>
#include <vector>
using namespace std;

void abc(int T)
{
	int N;
	cin >> N;

	vector<int>v(N);
	
	for (int &x : v) {
		cin >> x;
	}

	int M;
	cin >> M;
	

	char order;
	int x, y, num;
	for (int idx = 0; idx < M; idx++) {
		cin >> order;
		if (order == 'I') {
			cin >> x >> y;
			vector<int> inserted(y);
			for (int j = 0; j < y; j++) {
				cin >> inserted[j];
			}
			v.insert(v.begin() + x, inserted.begin(), inserted.end());
		}
		else if (order == 'D') {
			cin >> x >> y;
			v.erase(v.begin() + x, v.begin() + x + y);
		}
		else if (order == 'A') {
			cin >> y;
			for (int j = 0; j < y; j++) {
				cin >> num;
				v.push_back(num);
			}
		}
	}

	
	cout << "#" << T << ' ';
	for (int i = 0; i < 10 && i < v.size(); i++) {
		cout << v[i] << ' ';
	}
	cout << '\n';
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	for (int x = 1; x <= 10; x++) {
		abc(x);
	}

	return 0;
}