#include <iostream>

using namespace std;

void p1() {
    // Problem 1 : Check Prime - https://www.codingninjas.com/studio/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf 

    // run the loop till only sqrt(n) 
    // T(n) will become sqrt(n) 

    int n = 45;

	if (n == 1) {
        cout << 0 << endl;
        return;
    }

	for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            cout << 0 << endl;
            return;
        }
    }

	cout << 1 << endl;
}


int main() {
    // Day 016 

    p1();

    return 0;
}