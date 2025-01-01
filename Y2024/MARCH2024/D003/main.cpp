#include <iostream>
#include <vector>

using namespace std;

void moveZeroes(vector<int>& nums) {
    int ptr1 = 0, ptr2 = 0;

    while (ptr1 < nums.size()) {
        if (nums[ptr1] == 0) break;
        ptr1++;
    }

    ptr2 = ptr1 + 1;

    // ptr 1 is for sure is on 0 element 
    // ptr 2 is next to ptr 1 

    while (ptr2 < nums.size()) {
        if (nums[ptr2] != 0) {
            swap(nums[ptr1], nums[ptr2]);
            ptr1++;
            ptr2++;
        } else {
            ptr2++;
        }
    }

    // DRY 
    // {0, 1, 3, 5, 1, 0, 0, 3, 0}
    // {p1 : 0, p2 : 1, 3, 5, 1, 0, 0, 3, 0}
    // {1, p1: 0, p2: 3, 5, 1, 0, 0, 3, 0}
    // {1, 3, p1: 0, p2: 5, 1, 0, 0, 3, 0}
    // {1, 3, 5, p1: 0, p2: 1, 0, 0, 3, 0}
    // {1, 3, 5, 1, p1: 0, p2: 0, 0, 3, 0}
    // {1, 3, 5, 1, p1: 0, 0, p2: 0, 3, 0}
    // {1, 3, 5, 1, 3, p1: 0, 0, 0, p2: 0}
    // {1, 3, 5, 1, 3, p1: 0, 0, 0, 0, p2: NULL}
}

void p1() {
    // Problem 1 : 283 Move Zeroes - https://leetcode.com/problems/move-zeroes/description/ 

    vector<int> arr = {0, 1, 3, 5, 1, 0, 0, 3, 0};
    moveZeroes(arr);

    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 3 

    p1();


    return 0;
}