#include <iostream>

using namespace std;

bool isPowerOfTwo_Solution1(int N) {
    if (N == 0) return false;
    long long n = (long long) N - 1;

    while (n != 0) {
        if (!(n & 1)) return false;
        n = n >> 1;
    }

    return true;
}

bool isPowerOfTwo(int n) {
    if (n == 0) return false;

    long long N = n;
    return !(N & (N - 1));
}

void p1() {
    // Problem 1 : Leetcode 231. Power of Two - https://leetcode.com/problems/power-of-two/

    int n = 45;
    bool check = isPowerOfTwo(n);
    cout << check << endl;
}

int main() {
    // Day 2 

    p1();


    return 0;
}
