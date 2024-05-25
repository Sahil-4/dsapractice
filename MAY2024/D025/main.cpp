#include <iostream>
#include <vector>

using namespace std;

int longestOnes_solution1(vector<int>& nums, int k) {
    int n = nums.size();
    int maxOnesCount = 0;

    for (int i = 0; i < n; i++) {
        int onesCount = 0;
        int tempK = k;

        for (int j = i; j < n; j++) {
            if (tempK == 0 && nums[j] != 1) break;

            if (nums[j] != 1) tempK--;
            onesCount++;
        }

        if (maxOnesCount < onesCount) maxOnesCount = onesCount;
    }

    return maxOnesCount;

    // Complexity 
    // Time : O(n * n) 
    // Space : O(1) 
}

int longestOnes(vector<int>& nums, int k) {
    int n = nums.size();
    if (k == n) return n;
    int maxLen = 0;

    int l = 0, zeroesCount = 0;

    for (int r = 0; r < n; r++) {
        if (nums[r] == 0) zeroesCount++;

        while (nums[r] == 0 && zeroesCount > k) {
            if (nums[l++] == 0) zeroesCount--;
        }

        if (zeroesCount <= k) maxLen = max(maxLen, r - l + 1);
    }

    return maxLen;
}

void p1() {
    // Problem 1 : Leetcode 1004. Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1 

    vector<int> nums = {};
    int k = 2;

    int maxCons1 = longestOnes(nums, k);
    cout << "ans :: " << maxCons1 << endl;
}

int main() {
    // Day 25 

    p1();


    return 0;
}