#include <iostream>

using namespace std;

int minBitFlips(int start, int goal) {
    int count = 0;

    while (start != 0 || goal != 0) {
        if ((start & 1) ^ (goal & 1)) count++;

        start >>= 1;
        goal >>= 1;
    }

    return count;
}

void p1() {
    // Problem 1 : Leetcode 2220. Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/ 

    int start = 45;
    int goal = 54;

    int differentBits = minBitFlips(start, goal);
    cout << differentBits << endl;
}

int main() {
    // Day 5 

    p1();


    return 0;
}