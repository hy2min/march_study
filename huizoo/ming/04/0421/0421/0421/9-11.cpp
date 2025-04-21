#include <iostream>
using namespace std;

struct Person {
	int age;
	int height;
};

Person a;
Person b;


void input() {
	cin >> a.age >> a.height >> b.age >> b.height;

}

void output() {

	cout << (a.age + b.age) / 2;
	cout << ' ' << (a.height + b.height) / 2;

}

int main()
{
	input();
	output();




	return 0;
}