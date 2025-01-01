#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

void nextPermutation(vector<int>& nums) {
    int piv_index = -1;
    for (int i = nums.size() - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) {
            piv_index = i;
            break;
        }
    }

    if (piv_index == -1) return reverse(nums.begin(), nums.end());

    for (int i = nums.size() - 1; i > piv_index; i--) {
        if (nums[i] > nums[piv_index]) {
            swap(nums[i], nums[piv_index]);
            break;
        }
    }

    reverse(nums.begin() + piv_index + 1, nums.end());
}

void p1() {
    // Problem 1 : Next permutation - https://leetcode.com/problems/next-permutation/description/ 

    // vector<int> arr = {1, 2, 3};
    // vector<int> arr = {3, 2, 1};
    vector<int> arr = {2, 2, 4, 5, 6, 8};

    nextPermutation(arr);

    for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
    cout << endl;
}

int main() {
    // Day 9 

    p1();


    return 0;
}