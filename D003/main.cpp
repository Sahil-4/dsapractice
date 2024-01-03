#include <iostream>
#include <vector>

using namespace std;

void p1() {
    // Problem 1 : Leetcode 136 - https://leetcode.com/problems/single-number/solutions/ 

    vector<int> nums = {2, 2, 0, 0, 6, 6, 7, 8, 9, 9, 8}; 

    int ans = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        ans = ans ^ nums[i];
    }

    cout << ans << endl;
}

void p2() {
    // Problem 1 : Leetcode 2220 - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

    int start = 10, goal = 7; // out : 3 
    // start = 3, goal = 4; // out : 3 
    int count = 0;

    /*
    while (start != goal) {
        int l_bit_goal = goal&1;
        int l_bit_start = start&1;

        if (l_bit_goal != l_bit_start) {
            count++;
        }

        start = start >> 1;
        goal = goal >> 1;
    }
    */

    int diff = start ^ goal;
    while (diff != 0) {
        if (diff&1) {
            count ++;
        }

        diff >>= 1; // same as diff = diff >> 1 
    }

    cout << count << endl;
}


int main() {
    // Day 003 dsa practice 

    // p1();

    p2();

    return 0;
}