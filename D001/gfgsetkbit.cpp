#include <iostream>

using namespace std;

void p1() {
    // GFG - Set kth bit - https://practice.geeksforgeeks.org/problems/set-kth-bit3724/1

    int n = 15, k = 3; // output : 15

    int a = 1;

    // left shift and create a number which has only kth bit set 
    a = a << k;

    // now perform OR operation 
    int o = a | n;

    cout << o << endl;
}


int main() {
    p1();

    return 0;
}