#include <iostream>
using namespace std;


struct PROJECT {
	int num;
	char id;
	int vect[4];
};

PROJECT Z;

int main()
{
	int a;

	cin >> a;
	if (a>=0 && a<10){
		Z.num = 5;
		Z.id = 'G';
		Z.vect[0] = 1;
		Z.vect[1] = 2;
		Z.vect[2] = 3;
		Z.vect[3] = 4;
	}
	else if(a>=10 && a<100){
		Z.num = 8;
		Z.id = 'T';
		Z.vect[0] = 5;
		Z.vect[1] = 1;
		Z.vect[2] = 2;
		Z.vect[3] = 3;
	}
	else if(a>=100) {
		Z.num = 10;
		Z.id = 'Q';
		Z.vect[0] = 9;
		Z.vect[1] = 1;
		Z.vect[2] = 6;
		Z.vect[3] = 2;
	}

	cout << Z.num << endl << Z.id << endl;
	for (int x = 0; x < 4; x++) {
		cout << Z.vect[x] << ' ';
	}





	return 0;

}