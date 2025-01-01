#include <iostream>

using namespace std;

long long myPow(long long x, long long n) {
    int mod = 1000000007;

    if (n == 0) return 1;
    if (n == 1) return x;

    long long ans = myPow(x, n/2);
    ans = ((ans % mod) * (ans % mod)) % mod;
    if (n & 1) ans = ans * x;

    return ans % mod;
}

int countGoodNumbers(long long n) {
    if (n == 0) return 0;
    if (n == 1) return 5;

    int mod = 1000000007;

    long long evens = (n / 2) + (n % 2);
    long long odds = n / 2;

    long long a = myPow(5, evens);
    long long b = myPow(4, odds);

    return ((a % mod) * (b % mod)) % mod;
}

void p1() {
    // Problem 1 : Leetcode 1922. Count Good Numbers - https://leetcode.com/problems/count-good-numbers/ 

    int n = 10000000000;

    int ans = countGoodNumbers(n);
    cout << ans << endl;
}


int main() {
    // Day 19 

    p1();


    return 0;
}