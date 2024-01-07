#include <iostream>

using namespace std;

int _gcd(int big, int small) {
    if (big == 0 || small == 0) return small || big;
    if (big == 1 || small == 1) return 1;

    int r = big % small;

    if (r == 0) return small;

    big = small >= r ? small : r;
    small = small <= r ? small : r;
    return _gcd(big, small);
}

void p1() {
    // Problem 1 : Leetcode 1979 Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/ 

    // first find the smallest and largest number in the array 
    // then find the gcd 

    // int arr[] = {2,5,6,9,10}; // out : 2 
    int arr[] = {7,5,6,8,3}; // out : 1 
    int a = arr[0];
    int b = arr[0];

    // find the smallest and biggest number 
    for (int i = 1; i < sizeof(arr)/sizeof(arr[0]); i++) {
        // for small 
        if (a > arr[i]) {
            a = arr[i];
        }
        // for big 
        if (b < arr[i]) {
            b = arr[i];
        }
    }

    cout << "small : " << a << " big : " << b << endl;

    // find gcd 
    int gcd = _gcd(b, a);
    cout << "gcd : " << gcd << endl;
}

void p2() {
    // Problem 2 : Equilibrium Point - https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

    // int arr[] = {1,3,5,2,2};
    // int size = 5;
    // out 3 
    int arr[] = {1};
    int size = 1;
    // out 1 

    int l_sum = 0, r_sum = 0;
    int eq = -1;

    // edge cases 
    if (size == 0) {
        cout << -1 << endl;
        return;
    }
    if (size == 1) {
        cout << 1 << endl; 
        return;
    }

    for (int i = 0; i < size; i++) {
        r_sum += arr[i];
    }

    for (int i = 0; i < size; i++) {
        r_sum -= arr[i];
        if (l_sum == r_sum) {
            eq = i+1;
            break;;
        }
        l_sum += arr[i];
    }

    cout << eq << endl;
}

int main() {
    // Day 007 

    // p1();

    p2();

    return 0;
}