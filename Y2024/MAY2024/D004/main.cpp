#include <iostream>
#include <limits.h>

using namespace std;

int divide_solution1(int dividend, int divisor) {
    if (dividend == divisor) return 1;

    bool isPositive = true;
    if (dividend >= 0 && divisor < 0) isPositive = false;
    else if (dividend < 0 && divisor >= 0) isPositive = false;

    long long p = abs(dividend);
    long long q = abs(divisor);

    long long answer = 0;

    while (p >= q) {
        int a = 0;
        while (p >= (q << (a + 1))) a++;
        answer += 1 << a;
        p -= q << a;
    }

    if (answer == (1<<31) && isPositive) return INT_MAX;
    if (answer == (1<<31) && !isPositive) return INT_MIN;

    return isPositive ? answer : -answer;
}

int divide(int dividend, int divisor) {
    int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;

    long long p = abs(dividend);
    long long q = abs(divisor);

    long long answer = 0;
    long long temp = 0;

    for (int i = 31; i >= 0; i--) {
        if (temp + (q << i) <= p) {
            temp += q << i;
            answer += 1 << i;
        }
    }

    if (answer == (1 << 31) && sign == 1) return INT_MAX;
    if (answer == (1 << 31) && sign == -1) return INT_MIN;
    return sign * answer;
}

void p1() {
    // Problem 1 : Leetcode 29. Divide Two Integers - https://leetcode.com/problems/divide-two-integers/ 

    int ans = divide(45, -5); // -9 

    cout << ans << endl;
}

int main() {
    // Day 4 

    p1();


    return 0;
}