#include <iostream>
#include <vector>

using namespace std;


void solution() {
    // Leetcode 1009 Complement of Integer - https://leetcode.com/problems/complement-of-base-10-integer/

    int n = 10; // binary = 10 -> {1 0 1 0} -> {0 1 0 1} -> 5 

    if (n == 0 || n == 1) {
        return;
        // output is !n 
        cout << !n << endl;
    }

    int output = 0;
    int p = 1;

    while (n != 0) {
        // get bit 
        int bit = n&1;

        // flip the 
        bit = !bit;

        // create result 
        output += bit*p;

        // multiply power by 2 
        p = p << 1;

        // devide n by 2 
        n = n >> 1;
    }

    // return decimal 
    cout << output << endl;
}


int main() {
    solution();

    return 0;
}