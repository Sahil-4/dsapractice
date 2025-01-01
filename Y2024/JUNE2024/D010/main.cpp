#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int idx = n - 2;

    while (idx >= 0) {
        if (nums[idx] < nums[idx + 1]) break;
        idx--;
    }

    if (idx == -1) return reverse(nums.begin(), nums.end());

    for (int i = n - 1; i > idx; i--) {
        if (nums[i] > nums[idx]) {
            swap(nums[idx], nums[i]);
            break;
        }
    }

    reverse(nums.begin() + idx + 1, nums.end());
}

void p1() {
    // Problem 1 : Leetcode 31 Next permutation - https://leetcode.com/problems/next-permutation/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/next-permutation5226/1 

    vector<int> nums = {2, 3, 1, 5, 4};
    cout << "next purmutation for :: ";
    for (int i = 0; i < nums.size(); i++) cout << nums[i] << " ";
    cout << endl;
    nextPermutation(nums);
    for (int i = 0; i < nums.size(); i++) cout << nums[i] << " ";
    cout << endl;
}

int main() {
    // Day 10 

    p1();


    return 0;
}