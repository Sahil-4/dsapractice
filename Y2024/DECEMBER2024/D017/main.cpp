#include <bits/stdc++.h>

using namespace std;

bool recursion(vector<int>& nums, int index, int sum, int tsum) {
    if (sum == tsum) return true;
    if (sum > tsum) return false;
    if (index >= nums.size()) return false;

    bool not_pick = recursion(nums, index + 1, sum, tsum);
    bool pick = recursion(nums, index + 1, sum + nums[index], tsum);

    return pick | not_pick;

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) stack 
}

bool memoize(vector<int>& nums, int index, int sum, int tsum, vector<vector<int>>& dp) {
    if (sum == tsum) return true;
    if (sum > tsum) return false;
    if (index >= nums.size()) return false;

    if (dp[index][sum] != -1) return dp[index][sum];

    bool not_pick = memoize(nums, index + 1, sum, tsum, dp);
    bool pick = memoize(nums, index + 1, sum + nums[index], tsum, dp);

    bool out = pick | not_pick;
    dp[index][sum] = out ? 1 : 0;

    return out;

    // Complexity analysis 
    // Time : O(2*N) 
    // Space : O(N) stack + O(N*tsum) 
}

bool tabulation(vector<int>& nums, int ttsum) {
    int N = nums.size();

    vector<vector<bool>> dp(N + 1, vector<bool>(ttsum + 1, false));

    int tsum = ttsum / 2;

    // base case 
    for (int i = 0; i <= N; i++) dp[i][tsum] = true;
    // others - handled 

    for (int index = N - 1; index >= 0; index--) {
        for (int sum = tsum - 1; sum >= 0; sum--) {
            bool not_pick = dp[index + 1][sum];
            bool pick = false;
            if (sum + nums[index] <= ttsum) pick = dp[index + 1][sum + nums[index]];
            dp[index][sum] = pick | not_pick;
        }
    }

    return dp[0][0];

    // Complexity analysis 
    // Time : O(N*tsum) 
    // Space : O(N*ttsum) 
}

bool canPartition(vector<int> nums) {
    int N = nums.size();
    int tsum = accumulate(nums.begin(), nums.end(), 0);

    if (tsum & 1) return false;

    // recursion 
    // return recursion(nums, 0, 0, tsum/2);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(tsum+1, -1));
    // return memoize(nums, 0, 0, tsum/2, dp);

    // tabulation 
    return tabulation(nums, tsum);
}

void p1() {
    // Problem 1 : Leetcode 416. Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1 

    cout << canPartition({ 2,5,13 }) << endl;
    cout << canPartition({ 2,5,14 }) << endl;
    cout << canPartition({ 12,14,14 }) << endl;
    cout << canPartition({ 12,14,6, 14, 6 }) << endl;
}


int main() {
    // Day 17 of December 

    p1();


    return 0;
}