#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>& nums, int target) {
    int l = 0, h = nums.size() - 1;

    int m = l + (h - l) / 2;

    while (l <= h) {
        if (nums[m] == target) return m;
        else if (nums[m] < target) l = m + 1;
        else h = m - 1;

        m = l + (h - l) / 2;
    }

    return -1;
}

void p1() {
    // Problem 1 : binary search - https://leetcode.com/problems/binary-search/ 

    vector<int> nums = {-1,0,3,5,9,12};
    int target = 11;

    int index = search(nums, target);
    cout << index << endl;
}

int searchInsert(vector<int>& nums, int target) {
    int l = 0, h = nums.size() - 1;

    int m = l + ((h - l) / 2);

    while (l <= h) {
        if (nums[m] == target) return m;
        else if (nums[m] < target) l = m + 1;
        else h = m - 1;

        m = l + (h - l) / 2;
    }

    if (m == -1) return 0;
    if (m >= nums.size()) return nums.size();
    if (nums[m] < target) return m + 1;
    return m;
}

void p2() {
    // P2 search element - https://leetcode.com/problems/search-insert-position/ 

    vector<int> nums = {-1,0,3,5,9,12};
    int target = 11;

    int index = searchInsert(nums, target);
    cout << index << endl;
}


int main() {
    // Day 19 

    p1();

    p2();


    return 0;
}