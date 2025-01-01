#include <iostream>
#include <vector>

using namespace std;

int recursion(vector<vector<int>>& grid, int r, int c1, int c2, int rs, int cs) {
    if ((c1 < 0 || c1 >= cs) || (c2 < 0 || c2 >= cs)) return ((int)(-1e9));
    if (r == rs - 1) {
        if (c1 == c2) return grid[r][c1];
        return grid[r][c1] + grid[r][c2];
    }

    int maxPick = ((int)(-1e9));

    for (int d1 = -1; d1 <= 1; d1++) {
        for (int d2 = -1; d2 <= 1; d2++) {
            int pickup = recursion(grid, r + 1, c1 + d1, c2 + d2, rs, cs);
            maxPick = max(maxPick, pickup);
        }
    }

    maxPick += grid[r][c1];
    if (c1 != c2) maxPick += grid[r][c2];

    return maxPick;

    // Complexity analysis 
    // Time : O(9^N) 
    // Space : O(N) stack space 
}

int memoization(vector<vector<int>>& grid, int r, int c1, int c2, int rs, int cs, vector<vector<vector<int>>>& dp) {
    if ((c1 < 0 || c1 >= cs) || (c2 < 0 || c2 >= cs)) return -1;
    if (r == rs - 1) {
        if (c1 == c2) return grid[r][c1];
        return grid[r][c1] + grid[r][c2];
    }

    if (dp[r][c1][c2] != -1) return dp[r][c1][c2];

    int maxPick = -1;

    for (int d1 = -1; d1 <= 1; d1++) {
        for (int d2 = -1; d2 <= 1; d2++) {
            int pickup = memoization(grid, r + 1, c1 + d1, c2 + d2, rs, cs, dp);
            maxPick = max(maxPick, pickup);
        }
    }

    maxPick += grid[r][c1];
    if (c1 != c2) maxPick += grid[r][c2];

    return dp[r][c1][c2] = maxPick;

    // Complexity analysis 
    // Time : O(9*N) 
    // Space : O(N) stack space + O(rows*cols*cols) for memoization 
}

int tabulation(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();

    vector<vector<vector<int>>> dp(rows, vector<vector<int>>(cols, vector<int>(cols, 0)));

    // base case - bottom up 
    for (int c1 = 0; c1 < cols; c1++) {
        for (int c2 = 0; c2 < cols; c2++) {
            dp[rows - 1][c1][c2] = grid[rows - 1][c1];
            if (c1 != c2) {
                dp[rows - 1][c1][c2] += grid[rows - 1][c2];
            }
        }
    }

    for (int r = rows - 2; r >= 0; r--) {
        for (int c1 = 0; c1 < cols; c1++) {
            for (int c2 = 0; c2 < cols; c2++) {
                int bestPick = 0;

                for (int d1 = -1; d1 <= 1; d1++) {
                    for (int d2 = -1; d2 <= 1; d2++) {
                        int pickup = 0;
                        pickup += grid[r][c1];
                        if (c1 != c2) pickup += grid[r][c2];

                        if ((c1 + d1 >= 0 && c1 + d1 < cols) && (c2 + d2 >= 0 && c2 + d2 < cols)) {
                            pickup += dp[r + 1][c1 + d1][c2 + d2];
                        }
                        else {
                            pickup = -1;
                        }

                        bestPick = max(bestPick, pickup);
                    }
                }

                dp[r][c1][c2] = bestPick;
            }
        }
    }

    return dp[0][0][cols - 1];

    // Complexity analysis 
    // Time : O(rows * cols * cols) 
    // Space : O(rows * cols * cols) for tabulation 
}

int optimised(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();

    vector<vector<int>> dp(cols, vector<int>(cols, 0));

    // base case - bottom up 
    for (int c1 = 0; c1 < cols; c1++) {
        for (int c2 = 0; c2 < cols; c2++) {
            dp[c1][c2] = grid[rows - 1][c1];
            if (c1 != c2) {
                dp[c1][c2] += grid[rows - 1][c2];
            }
        }
    }

    for (int r = rows - 2; r >= 0; r--) {
        vector<vector<int>> curr(cols, vector<int>(cols, 0));

        for (int c1 = 0; c1 < cols; c1++) {
            for (int c2 = 0; c2 < cols; c2++) {
                int bestPick = 0;

                for (int d1 = -1; d1 <= 1; d1++) {
                    for (int d2 = -1; d2 <= 1; d2++) {
                        int pickup = 0;
                        pickup += grid[r][c1];
                        if (c1 != c2) pickup += grid[r][c2];

                        if ((c1 + d1 >= 0 && c1 + d1 < cols) && (c2 + d2 >= 0 && c2 + d2 < cols)) {
                            pickup += dp[c1 + d1][c2 + d2];
                        }
                        else {
                            pickup = -1;
                        }

                        bestPick = max(bestPick, pickup);
                    }
                }

                curr[c1][c2] = bestPick;
            }
        }

        dp = curr;
    }

    return dp[0][cols - 1];

    // Complexity analysis 
    // Time : O(rows * cols * cols) 
    // Space : O(2 * cols * cols) for tabulation 
}

int cherryPickup(vector<vector<int>>& grid) {
    // grid dimensions 
    // int rows = grid.size();
    // int cols = grid[0].size();

    // recursion 
    // return recursion(grid, 0, 0, cols - 1, rows, cols);

    // memoization 
    // vector<vector<vector<int>>> dp(rows, vector<vector<int>>(cols, vector<int>(cols, -1)));
    // return memoization(grid, 0, 0, cols - 1, rows, cols, dp);

    // tabulation 
    // return tabulation(grid);

    // space optimised 
    return optimised(grid);
}

void p1() {
    // Problem 1 : Leetcode 1463. Cherry Pickup II - https://leetcode.com/problems/cherry-pickup-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/chocolates-pickup/1 

    vector<vector<int>> grid = { {8,8,10,9,1,7},{8,8,1,8,4,7},{8,6,10,3,7,7},{3,0,9,3,2,7},{6,8,9,4,2,5},{1,1,5,8,8,1},{5,6,5,2,9,9},{4,4,6,2,5,4},{4,4,5,3,1,6},{9,2,2,1,9,3} };

    int cs = cherryPickup(grid);
    cout << cs << endl;
}

int main() {
    // Day 11 of DP 

    p1();


    return 0;
}