#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<int>& nums, int i, int j) {
        if (i > j) return 0;

        int mcoins = INT_MIN;

        for (int k = i; k <= j; k++) {
            int lc = recursion(nums, i, k - 1);
            int rc = recursion(nums, k + 1, j);
            int tc = nums[i - 1] * nums[k] * nums[j + 1];
            int coins = lc + tc + rc;
            mcoins = max(mcoins, coins);
        }

        return mcoins;

        // Complexity analysis 
        // Time : O(2^N * N) 
        // Space : O(N) 
    }

    int memoize(vector<int>& nums, int i, int j, vector<vector<int>>& dp) {
        if (i > j) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int mcoins = INT_MIN;

        for (int k = i; k <= j; k++) {
            int lc = memoize(nums, i, k - 1, dp);
            int rc = memoize(nums, k + 1, j, dp);
            int tc = nums[i - 1] * nums[k] * nums[j + 1];
            int coins = lc + tc + rc;
            mcoins = max(mcoins, coins);
        }

        return dp[i][j] = mcoins;

        // Complexity analysis 
        // Time : O(2*N*N*N) 
        // Space : O(N) + O(N*N) 
    }

    int tabulation(vector<int>& nums, int N) {
        vector<vector<int>> dp(N + 3, vector<int>(N + 3, 0));

        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= N; j++) {
                if (i > j) continue;

                int mcoins = INT_MIN;

                for (int k = i; k <= j; k++) {
                    int lc = dp[i][k - 1];
                    int rc = dp[k + 1][j];
                    int tc = nums[i - 1] * nums[k] * nums[j + 1];
                    int coins = lc + tc + rc;
                    mcoins = max(mcoins, coins);
                }

                dp[i][j] = mcoins;
            }
        }

        return dp[1][N];

        // Complexity analysis 
        // Time : O(N*N*N) 
        // Space : O(N*N) 
    }

public:
    int maxCoins(vector<int> nums) {
        int N = nums.size();
        // can be erase before returning output 
        nums.insert(nums.begin(), 1);
        nums.push_back(1);

        // return recursion(nums, 1, N);

        // vector<vector<int>> dp(N+3, vector<int>(N+3, -1));
        // return memoize(nums, 1, N, dp);

        return tabulation(nums, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 312. Burst Balloons - https://leetcode.com/problems/burst-balloons/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/burst-balloons/1 

    cout << Problem1().maxCoins({ 3,1,5,8 }) << endl;
}


int main() {
    // Day 27 of December 

    p1();


    return 0;
}