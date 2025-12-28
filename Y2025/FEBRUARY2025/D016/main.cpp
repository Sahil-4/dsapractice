#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<vector<int>>& tri, int r = 0, int c = 0) {
        if (r == tri.size()) return 0;

        int opA = recursion(tri, r + 1, c);
        int opB = recursion(tri, r + 1, c + 1);

        return tri[r][c] + min(opA, opB);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack 
    }

    int memoize(vector<vector<int>>& tri, vector<vector<int>>& dp, int r = 0, int c = 0) {
        if (r == tri.size()) return 0;

        if (dp[r][c] != -1) return dp[r][c];

        int opA = memoize(tri, dp, r + 1, c);
        int opB = memoize(tri, dp, r + 1, c + 1);

        int out = tri[r][c] + min(opA, opB);

        return dp[r][c] = out;

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(N) stack + O(N*N) memory 
    }

    int tabulation(vector<vector<int>>& tri) {
        int N = tri.size();

        vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));

        // base case - already handled 

        // recurrence 
        for (int r = N - 1; r >= 0; r--) {
            for (int c = r; c >= 0; c--) {
                int opA = dp[r + 1][c];
                int opB = dp[r + 1][c + 1];

                int out = tri[r][c] + min(opA, opB);

                dp[r][c] = out;
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N*N) stack 
    }

    int optimised(vector<vector<int>>& tri) {
        int N = tri.size();

        vector<int> next(N + 1, 0);

        // base case - already handled 

        // recurrence 
        for (int r = N - 1; r >= 0; r--) {
            vector<int> curr(N + 1, 0);
            for (int c = r; c >= 0; c--) {
                int opA = next[c];
                int opB = next[c + 1];

                int out = tri[r][c] + min(opA, opB);

                curr[c] = out;
            }

            next = curr;
        }

        // return 
        return next[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(2*N) stack 
    }

public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // return recursion(triangle);

        // int N = triangle.size();

        // vector<vector<int>> dp(N, vector<int>(N, -1));
        // return memoize(triangle, dp);

        // return tabulation(triangle);

        return optimised(triangle);
    }
};

void p1() {
    // Problem 1 : Leetcode 120. Triangle - https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/triangle-path-sum/1 

    vector<vector<int>> triangle = { {2},{3,4},{6,5,7},{4,1,8,3} };
    cout << Problem1().minimumTotal(triangle) << endl;
}

class Problem2 {
    int BOUND = (int)(1e9) + 7;

    int recursion(vector<vector<int>>& grid, int i = 0, int j = 0) {
        if (i == grid.size() - 1 && j == grid[0].size() - 1) return grid[i][j];
        if (i >= grid.size() || j >= grid[0].size()) return BOUND;

        int left = grid[i][j] + recursion(grid, i, j + 1);
        int bottom = grid[i][j] + recursion(grid, i + 1, j);

        return min(left, bottom);

        // Complexity analysis 
        // Time : O(2^(N+M)) 
        // Space : O(N+M) stack 
    }

    int memoize(vector<vector<int>>& grid, vector<vector<int>>& dp, int i = 0, int j = 0) {
        if (i == grid.size() - 1 && j == grid[0].size() - 1) return grid[i][j];
        if (i >= grid.size() || j >= grid[0].size()) return BOUND;

        if (dp[i][j] != -1) return dp[i][j];

        int left = grid[i][j] + memoize(grid, dp, i, j + 1);
        int bottom = grid[i][j] + memoize(grid, dp, i + 1, j);

        return dp[i][j] = min(left, bottom);

        // Complexity analysis 
        // Time : O(2*(N*M)) 
        // Space : O(N+M) stack + O(N*M) memory 
    }

    int tabulation(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size();
        vector<vector<int>> dp(N + 1, vector<int>(M + 1, BOUND));

        // base - done 
        dp[N - 1][M - 1] = grid[N - 1][M - 1];

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            for (int j = M - 1; j >= 0; j--) {
                if (i == N - 1 && j == M - 1) continue;

                int left = grid[i][j] + dp[i][j + 1];
                int bottom = grid[i][j] + dp[i + 1][j];

                dp[i][j] = min(left, bottom);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) memory 
    }

public:
    int minPathSum(vector<vector<int>>& grid) {
        // return recursion(grid);

        // int N = grid.size(), M = grid[0].size();
        // vector<vector<int>> dp(N, vector<int>(M, -1));
        // return memoize(grid, dp);

        return tabulation(grid);
    }
};

void p2() {
    // Problem 2 : Leetcode 64. Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<int>> grid = { {1,3,1},{1,5,1},{4,2,1} };
    cout << Problem2().minPathSum(grid) << endl;
}


int main() {
    // Day 16 of February 

    p1();

    p2();


    return 0;
}