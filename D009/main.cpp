#include <iostream>
#include <string>
#include <limits.h>


using namespace std;


void p1() {
    // Problem 1 : Binary number to decimal number - https://www.geeksforgeeks.org/problems/binary-number-to-decimal-number3525/1 

    // string str = "1011"; // 11 
    // string str = "10000001000111"; // 11 
    string str = "1000111110111"; // 4299 

    int ans = 0;
    int i = str.length()-1;
    int p = 1;

    while (i >= 0) {
        int b = str[i] == 49 ? 1 : 0;
        ans += b * p;
        i--;
        p <<= 1;
    }

    cout << ans << endl;
}

void p2() {
    // Problem 2 : Reverse Integer - https://leetcode.com/problems/reverse-integer/ 

    // int n = 1999999999;
    // int n = 12;
    // int n = -12;
    // int n = 0;
    // int n = 1;
    int n = -2147483412;
    int ans = 0;

    while (n != 0) {
        if (ans > INT_MAX/10 || ans < INT_MIN/10) {
            cout << 0 << endl;
            break;
        }

        ans = (ans * 10) + (n % 10);
        n /= 10;
    }

    cout << ans << endl;
}


int main() {
    // Day 009 

    // p1();

    p2();

    return 0;
}
