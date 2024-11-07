#include <iostream>
#include <vector>

using namespace std;

int recursion(vector<vector<int>>& grid, int r, int c) {
    // out of grid 
    if (r >= grid.size() || c >= grid[0].size()) return 0;
    // has obstacle 
    if (grid[r][c] == 1) return 0;
    // destination cell 
    if (r == grid.size() - 1 && c == grid[0].size() - 1) return 1;

    int rm = recursion(grid, r + 1, c);
    int dm = recursion(grid, r, c + 1);

    return rm + dm;

    // Complexity analysis 
    // Time : O(2^(m*n)) 
    // Space : O(m + n) stack space 
}

int memoization(vector<vector<int>>& grid, int r, int c, vector<vector<int>>& dp) {
    // out of grid 
    if (r >= grid.size() || c >= grid[0].size()) return 0;

    // has obstacle 
    if (grid[r][c] == 1) return 0;

    // destination cell 
    if (r == grid.size() - 1 && c == grid[0].size() - 1) return 1;

    if (dp[r][c] != -1) return dp[r][c];

    int rm = memoization(grid, r + 1, c, dp);
    int dm = memoization(grid, r, c + 1, dp);

    return dp[r][c] = (rm + dm);

    // Complexity analysis 
    // Time : O(m * n) 
    // Space : O(m * n) for dp + O(m + n) stack space 
}

int getDP(vector<vector<int>>& dp, int i, int j) {
    if (i < 0 || i >= dp.size() || j < 0 || j >= dp[0].size()) return 0;
    return dp[i][j];
}

int tabulation(vector<vector<int>>& grid, vector<vector<int>>& dp) {
    // grid dimensions 
    int m = grid.size(), n = grid[0].size();

    // if start or destination is not free - has obstacle 
    if (grid[0][0] == 1 || grid[m - 1][n - 1] == 1) return 0;

    dp[0][0] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;

            int um = getDP(dp, i - 1, j);
            int lm = getDP(dp, i, j - 1);
            dp[i][j] = lm + um;

            if (grid[i][j] == 1) dp[i][j] = 0;
        }
    }

    return dp[m - 1][n - 1];

    // Complexity analysis 
    // Time : O(m * n) 
    // Space : O(m * n) for dp 
}

int optimised(vector<vector<int>>& grid) {
    // grid dimensions 
    int m = grid.size(), n = grid[0].size();

    // if start or destination is not free - has obstacle 
    if (grid[0][0] == 1 || grid[m - 1][n - 1] == 1) return 0;

    vector<int> dp(n, 0);

    for (int i = 0; i < m; i++) {
        vector<int> tempo(n, 0);

        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                tempo[j] = 1;
                continue;
            }

            if (grid[i][j] != 1 && i > 0) tempo[j] += dp[j];
            if (grid[i][j] != 1 && j > 0) tempo[j] += tempo[j - 1];
        }

        dp = tempo;
    }

    return dp[n - 1];

    // Complexity analysis 
    // Time : O(m * n) 
    // Space : O(n) for dp (state) 
}

int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    // grid dimensions 
    int m = obstacleGrid.size(), n = obstacleGrid[0].size();

    // if start or destination is not free - has obstacle 
    if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1) return 0;

    // recursion 
    // return recursion(obstacleGrid, 0, 0);

    // memoization 
    // vector<vector<int>> dp(m, vector<int>(n, -1));
    // return memoization(obstacleGrid, 0, 0, dp);

    // tabulation 
    // vector<vector<int>> dp(m, vector<int>(n, 0));
    // return tabulation(obstacleGrid, dp);

    // space optimised 
    return optimised(obstacleGrid);
}

void p1() {
    // Problem 1 : Leetcode 63. Unique Paths II - https://leetcode.com/problems/unique-paths-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/grid-path-2/0 

    vector<vector<int>> grid = {
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    };

    int paths = uniquePathsWithObstacles(grid);
    cout << paths << endl;
}

int main() {
    // Day 7 of DP 

    p1();


    return 0;
}