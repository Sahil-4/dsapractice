#include <iostream>
#include <vector>

using namespace std;

void p1() {
    // Problem 1 : N-Forest - https://www.codingninjas.com/studio/problems/n-forest_6570177 
    int n = 5;

    for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << "* ";
		}
		cout << endl;
	}
}

void p2() {
    // Problem 2  : N/2-Forest - https://www.codingninjas.com/studio/problems/n-2-forest_6570178 

    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void p3() {
    // Problem 3 : N-Triangles - https://www.codingninjas.com/studio/problems/n-triangles_6573689 

    int n = 3;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cout << j << " ";
		}
		cout << endl;
	}
}

void p4() {
    // Problem 4 : Triangle - https://www.codingninjas.com/studio/problems/triangle_6573690 

    int n = 3;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cout << i << " ";
		}
		cout << endl;
	}
}

void p5() {
    // Problem 5 : Seeding - https://www.codingninjas.com/studio/problems/seeding_6581892 

    int n = 3;

	for (int i = n; i > 0; i--) {
		for (int j = i; j > 0; j--) {
			cout << "* ";
		}
		cout << endl;
	}
}

void p6() {
    // Problem 6 : Reverse Number Triangle - https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889 

    int n = 3;

    for (int i = n; i > 0; i--) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}



int main() {
    // Day 010 

    // p1();

    // p2();

    // p3();

    // p4();

    // p5();

    // p6();


    return 0;
}