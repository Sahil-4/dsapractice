#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int recursion(vector<vector<int>>& grid, int i, int j, int m, int n) {
    // out of grid
    if (i >= m || j >= n) return INT_MAX;
    // destination cell
    if (i == m - 1 && j == n - 1) return grid[i][j];

    int mr = recursion(grid, i, j + 1, m, n);
    int md = recursion(grid, i + 1, j, m, n);

    return grid[i][j] + min(mr, md);

    // Complexity analysis
    // Time : O(2^(m * n))
    // Space : O(m + n) recursion stack space
}

int memoization(vector<vector<int>>& grid, int i, int j, int m, int n, vector<vector<int>>& dp) {
    // out of grid
    if (i >= m || j >= n) return INT_MAX;

    // destination cell
    if (i == m - 1 && j == n - 1) return grid[i][j];

    if (dp[i][j] != -1) return dp[i][j];

    int mr = memoization(grid, i, j + 1, m, n, dp);
    int md = memoization(grid, i + 1, j, m, n, dp);

    int out = grid[i][j] + min(mr, md);

    return dp[i][j] = out;

    // Complexity analysis
    // Time : O(2 * (m + n))
    // Space : O(m + n) recursion stack space + O(m * n) for memoization
}

int getDP(vector<vector<int>>& dp, int i, int j) {
    if (i < 0 || i >= dp.size() || j < 0 || j >= dp[0].size()) return INT_MAX;
    return dp[i][j];
}

int tabulation(vector<vector<int>>& grid, vector<vector<int>>& dp) {
    int m = grid.size(), n = grid[0].size();

    dp[0][0] = grid[0][0];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;

            int mu = getDP(dp, i - 1, j);
            int ml = getDP(dp, i, j - 1);

            dp[i][j] = grid[i][j] + min(mu, ml);
        }
    }

    return dp[m - 1][n - 1];

    // Complexity analysis
    // Time : O(m * n)
    // Space : O(m * n) for tabulation
}

int optimised(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();

    vector<int> dp(n, INT_MAX);

    for (int i = 0; i < m; i++) {
        vector<int> tempo(n, INT_MAX);
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                tempo[0] = grid[0][0];
                continue;
            }

            // cost to move from left and up 
            int lm = INT_MAX;
            int um = INT_MAX;

            // we can move left wards 
            if (j > 0) lm = tempo[j - 1];

            // we can move up wards 
            if (i > 0) um = dp[j];

            // update path to current cell - min path sum 
            tempo[j] = grid[i][j] + min(lm, um);
        }

        dp = tempo;
    }

    return dp[n - 1];

    // Complexity analysis
    // Time : O(m * n)
    // Space : O(2n) for optimised tabulation
}

int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();

    // recursion
    // return recursion(grid, 0, 0, m, n);

    // memoization
    // vector<vector<int>> dp(m, vector<int>(n, -1));
    // return memoization(grid, 0, 0, m, n, dp);

    // tabulation
    // vector<vector<int>> dp(m, vector<int>(n, 0));
    // return tabulation(grid, dp);

    // space optimised
    return optimised(grid);
}

void p1() {
    // Problem 1 : Leetcode 64. Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/number-of-paths0926/1 

    vector<vector<int>> grid = { {1,3,1},{1,5,1},{4,2,1} };
    int cost = minPathSum(grid);
    cout << cost << endl;
}


int main() {
    // Day 8 of DP 

    p1();


    return 0;
}