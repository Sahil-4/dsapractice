#include <iostream>
#include <cmath>

using namespace std;

void p1() {
    // Problem 1 : Check Armstrong - https://www.codingninjas.com/studio/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf 

    int n = 12;

    // find k = number of digits 
    // find sum = digits raised to power k 
    // return true if sum == n 

    if (n == 0) {
        cout << "not arm strong" << endl;
        return;
    }

    int k = 0;
    int copy = n;
    while (copy > 0) {
        k++;
        copy /= 10;
    }

    copy = n;
    int sum = 0;
    while (copy > 0) {
        int d = copy % 10;
        sum += pow(d, k);
        copy /= 10;
    }

    if (sum == n) cout << "arm strong" << endl;
    if (sum != n) cout << "not arm strong" << endl;
}


int main() {
    // Day 015 

    p1();


    return 0;
}