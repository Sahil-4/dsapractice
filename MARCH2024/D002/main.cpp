#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int>& nums) {
    int count = 0;

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i - 1]) {
            count++;
        }
    }

    if (nums[nums.size() - 1] > nums[0]) count++;

    return count <= 1;
}

void p1() {
    // Problem 1 : Leetcode 1752 Check if Array Is Sorted and Rotated - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/ 

    // vector<int> arr = {1, 2, 3, 5, 7, 8};
    vector<int> arr = {5, 7, 8, 1, 2, 3};

    bool isSortedRotated = check(arr);
    cout << isSortedRotated << endl;
}

int main() {
    // Day 2 

    p1();


    return 0;
}