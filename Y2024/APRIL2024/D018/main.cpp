#include <iostream>

using namespace std;

double myPow(double x, int n) {
    if (n == 0) return 1;
    if (n == 1) return x;
    if (n == -1) return 1 / x;

    int d = abs(n);
    double ans = myPow(x, d/2);
    ans *= ans;
    if (d & 1) ans *= x;

    if (n < 0) return 1 / ans;
    return ans;
}

void p1() {
    // Problem 1 : Leetcode 50. Pow(x, n) - https://leetcode.com/problems/powx-n/ 
    // 99th question on leetcode 

    // double x = 2.00;
    // int n = 10;

    double x = 2.100;
    int n = 3;

    double ans = myPow(x, n);
    cout << ans << endl;
}


int main() {
    // Day 18 

    p1();


    return 0;
}
