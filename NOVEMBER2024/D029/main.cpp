#include <bits/stdc++.h>

using namespace std;

int recursion(vector<int>& nums, int i, int j) {
    if (i > j) return 0;

    int mcoins = INT_MIN;

    for (int k = i; k <= j; k++) {
        int coins = nums[i - 1] * nums[k] * nums[j + 1];
        int lcoins = recursion(nums, i, k - 1);
        int rcoins = recursion(nums, k + 1, j);

        int sum = coins + lcoins + rcoins;
        mcoins = max(mcoins, sum);
    }

    return mcoins;

    // Complexity analysis 
    // Time : O(2N^N) ~ 
    // Space : O(N) stack 
}

int memoize(vector<int>& nums, int i, int j, vector<vector<int>>& dp) {
    if (i > j) return 0;

    if (dp[i][j] != -1) return dp[i][j];

    int mcoins = INT_MIN;

    for (int k = i; k <= j; k++) {
        int coins = nums[i - 1] * nums[k] * nums[j + 1];
        int lcoins = memoize(nums, i, k - 1, dp);
        int rcoins = memoize(nums, k + 1, j, dp);

        int sum = coins + lcoins + rcoins;
        mcoins = max(mcoins, sum);
    }

    return dp[i][j] = mcoins;

    // Complexity analysis 
    // Time : O(2N*N) ~ 
    // Space : O(N) stack + O(N+1*N+1) memory 
}

int tabulation(vector<int>& nums, int N) {
    vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));

    // base - handled if (i>j) dp[i][j] = 0;

    // recurrence 
    for (int i = N; i >= 1; i--) {
        for (int j = i; j <= N; j++) {
            int mcoins = INT_MIN;

            for (int k = i; k <= j; k++) {
                int coins = nums[i - 1] * nums[k] * nums[j + 1];
                int lcoins = dp[i][k - 1];
                int rcoins = dp[k + 1][j];

                int sum = coins + lcoins + rcoins;
                mcoins = max(mcoins, sum);
            }

            dp[i][j] = mcoins;
        }
    }

    // return 
    return dp[1][N];

    // Complexity analysis 
    // Time : O(N*N*N) ~ 
    // Space : O(N+1*N+1) memory 
}

int maxCoins(vector<int>& nums) {
    int N = nums.size();

    nums.push_back(1);
    nums.insert(nums.begin(), 1);

    // recursion 
    // return recursion(nums, 1, N);

    // memoize 
    // vector<vector<int>> dp(N+1, vector<int>(N+1, -1));
    // return memoize(nums, 1, N, dp);

    // tabulation 
    return tabulation(nums, N);
}

void p1() {
    // Problem 1 : Leetcode 312. Burst Balloons - https://leetcode.com/problems/burst-balloons/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/burst-balloons/1 

    vector<int> nums = { 3,5,15,18 };

    int c = maxCoins(nums);
    cout << c << endl;
}


int main() {
    // Day 29 of DP 

    p1();


    return 0;
}