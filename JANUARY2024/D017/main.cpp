#include <iostream>

using namespace std;

int gcd(int n, int m) {
    // base cases 
    if (n == 0 || m == 0) return n > m ? n : m;
    if (n == 1 || m == 1) return 1;
    if (n == m) return n;

    // recursion 
    if (m > n) {
        return gcd(n, m-n);
    } else {
        return gcd(m, n-m);
    }
}

void p1() {
    // Problem 1 : GCD/HCF - https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf 

    // Eucledean's algo 
    // using recursion 

    // int n = 5, m = 13;
    // int n = 5, m = 10;
    // int n = 5, m = 2;
    // int n = 7, m = 14;
    int n = 700, m = 140;

    cout << gcd(n, m) << endl;
}


int main() {
    // Day 17 

    p1();


    return 0;
}