#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void rotate_Solution1B(vector<int>& nums, int k) {
    // left rotate 
    int n = nums.size();

    for (k; k > 0; k--) {
        int prev = nums[0];
        for (int i = n - 1; i >= 0; i--) {
            int temp = prev;
            prev = nums[i], nums[i] = temp;
        }
    }
}

void rotate_Solution1A(vector<int>& nums, int k) {
    // right rotate 
    int n = nums.size();

    for (k; k > 0; k--) {
        int prev = nums[n - 1];
        for (int i = 0; i < n; i++) {
            int temp = prev;
            prev = nums[i], nums[i] = temp;
        }
    }
}

void rotate_Solution2B(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> arr = nums;
    for (int i = 0; i < n; i++) arr[(n + i - k) % n] = nums[i];
}

void rotate_Solution2A(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> arr = nums;
    for (int i = 0; i < n; i++) nums[(i + k) % n] = arr[i];
}

void rotate_Solution3B(vector<int>& nums, int k) {
    int n = nums.size();
    k %= n;
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
    reverse(nums.begin(), nums.end());
}

void rotate(vector<int>& nums, int k) {
    // _Solution3A
    int n = nums.size();
    k %= n;
    reverse(nums.begin(), nums.begin() + n - k);
    reverse(nums.begin() + n - k, nums.end());
    reverse(nums.begin(), nums.end());
}

void p1() {
    // Problem 1 : Leetcode 189. Rotate Array - https://leetcode.com/problems/rotate-array/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1 

    vector<int> nums = {1,2,3,4,5,7,8,9};
    int k = 2;
    rotate(nums, k);
}

int main() {
    // Day 5 - revision 

    p1();


    return 0;
}