#include <iostream>
#include <vector>

using namespace std;


int recursion(vector<int>& nums, int index) {
    if (index >= nums.size()) return 0;

    int maxAmt = 0;

    for (int i = index; i < nums.size(); i++) {
        int amt = nums[i] + recursion(nums, i + 2);
        maxAmt = max(maxAmt, amt);
    }

    return maxAmt;

    // Complexity analysis 
    // Time : O(N^2) 
    // Space : O(N) for stack 
}

int memoization(vector<int>& nums, int index, vector<int>& dp) {
    if (index >= nums.size()) return 0;
    if (dp[index] != -1) return dp[index];

    int maxAmt = 0;

    for (int i = index; i < nums.size(); i++) {
        int amt = nums[i] + memoization(nums, i + 2, dp);
        maxAmt = max(maxAmt, amt);
    }

    return dp[index] = maxAmt;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) for stack + O(N) for dp 
}

int memoization2(vector<int>& nums, int index, vector<int>& dp) {
    // based on pick and not pick 

    if (index >= nums.size()) return 0;
    if (dp[index] != -1) return dp[index];

    int pick = nums[index] + memoization2(nums, index + 2, dp);
    int not_pick = memoization2(nums, index + 1, dp);

    return dp[index] = max(pick, not_pick);

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) for stack + O(N) for dp 
}

int dpe(vector<int>& dp, int index) {
    if (index < 0 || index >= dp.size()) return 0;
    return dp[index];
}

int tabulation(vector<int>& nums, int index, vector<int>& dp) {
    int N = nums.size();
    dp[0] = nums[0];

    for (int i = 1; i < N; i++) {
        int pick = nums[i] + dpe(dp, i - 2);
        int not_pick = 0 + dpe(dp, i - 1);
        dp[i] = max(pick, not_pick);
    }

    dp[N] = max(dpe(dp, N - 1), dpe(dp, N - 2));

    return dp[N];

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) for dp 
}

int memory_optimised(vector<int>& nums, int index) {
    int N = nums.size();

    int prev2 = 0;
    int prev1 = nums[0];

    for (int i = 1; i < N; i++) {
        int pick = nums[i] + prev2;
        int not_pick = prev1;

        prev2 = prev1;
        prev1 = max(pick, not_pick);
    }

    return max(prev2, prev1);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
}

int rob(vector<int>& nums) {
    // recursion 
    // return recursion(nums, 0);

    // memoization 
    // int N = nums.size() + 1;
    // vector<int> dp(N, -1);
    // return memoization(nums, 0, dp);
    // return memoization2(nums, 0, dp);

    // tabulation 
    // vector<int> dp(N, 0);
    // return tabulation(nums, 0, dp);

    // memory optimization 
    return memory_optimised(nums, 0);
}

void p1() {
    // Problem 1 : Leetcode 198. House Robber - https://leetcode.com/problems/house-robber/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1 

    vector<int> nums = { 1,2,3,1,2,5,4,8,6,5,2,0,5,8,4 };

    int amt = rob(nums);
    cout << amt << endl;
}


int main() {
    // Day 3 of DP 

    p1();


    return 0;
}