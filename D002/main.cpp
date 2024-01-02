#include <iostream>

using namespace std;


void p1() {
    // problem 1 : Leetcode 2595 - https://leetcode.com/problems/number-of-even-and-odd-bits/

    // Number of Even and Odd Bits

    int n = 12; // {0 1 1 0}
    n = 17; // out : [2 0]

    int arr[2] = {0, 0};
    int i = 0;

    while (n != 0) {
        if (n&1 && i & 1) {
            arr[1] = arr[1]+1;
        } else if (n&1 && !(i & 1)) {
            arr[0] = arr[0]+1;
        }

        n = n >> 1;
        i++;
    }

    cout << "even : " << arr[0] << " odd : " << arr[1] << endl;
}

void p2() {
    // problem 2 : Leetcode 191 - https://leetcode.com/problems/number-of-1-bits/

    uint32_t n = 00000000000000000000000000001011;

    int count = 0;

    for (int i = 0; i < 32; i++) {
        if ((n>>i)&1) {
            count++;
        }
    }

    cout << count << endl;
}

int main() {
    // Day 002 of DSA practice 

    // p1();

    p2();


    return 0;
}