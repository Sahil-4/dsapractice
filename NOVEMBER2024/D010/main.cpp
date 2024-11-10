#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int __recursion(vector<vector<int>>& matrix, int r, int c, int N) {
    if (c >= N || c < 0) return ((int)(1e9));
    if (r == N - 1) return matrix[r][c];

    int db = __recursion(matrix, r + 1, c, N);
    int dl = __recursion(matrix, r + 1, c - 1, N);
    int dr = __recursion(matrix, r + 1, c + 1, N);

    int out = matrix[r][c] + min(min(dl, dr), db);

    return out;
}

int recursion(vector<vector<int>>& matrix) {
    int out = INT_MAX;

    int N = matrix.size();

    for (int c = 0; c < N; c++) {
        int sum = __recursion(matrix, 0, c, N);
        out = min(out, sum);
    }

    return out;

    // Complexity analysis
    // Time : O(N * (3 ^ N))
    // Space : O(N) recursion stack space
}

int __memoization(vector<vector<int>>& matrix, int r, int c, int N, vector<vector<int>>& dp) {
    if (c >= N || c < 0) return ((int)(1e9));
    if (r == N - 1) return matrix[r][c];

    if (dp[r][c] != INT_MAX) return dp[r][c];

    int db = __memoization(matrix, r + 1, c, N, dp);
    int dl = __memoization(matrix, r + 1, c - 1, N, dp);
    int dr = __memoization(matrix, r + 1, c + 1, N, dp);

    int out = matrix[r][c] + min(min(dl, dr), db);

    return dp[r][c] = out;
}

int memoization(vector<vector<int>>& matrix) {
    int out = INT_MAX;

    int N = matrix.size();

    vector<vector<int>> dp(N, vector<int>(N, INT_MAX));

    for (int c = 0; c < N; c++) {
        int sum = __memoization(matrix, 0, c, N, dp);
        out = min(out, sum);
    }

    return out;

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(N) recursion stack space + O(N*N) for dp
}

int tabulation(vector<vector<int>>& matrix) {
    int N = matrix.size();
    vector<vector<int>> dp(N, vector<int>(N, 0));

    // 0th row - base case
    for (int c = 0; c < N; c++) {
        dp[0][c] = matrix[0][c];
    }

    for (int r = 1; r < N; r++) {
        for (int c = 0; c < N; c++) {
            // directly up - for down
            dp[r][c] = dp[r - 1][c];

            // diagonally left
            if (c > 0 && dp[r][c] > dp[r - 1][c - 1]) {
                dp[r][c] = dp[r - 1][c - 1];
            }

            // diagonally right
            if (c < N - 1 && dp[r][c] > dp[r - 1][c + 1]) {
                dp[r][c] = dp[r - 1][c + 1];
            }

            // add current cell 
            dp[r][c] += matrix[r][c];
        }
    }

    int out = INT_MAX;
    for (int c = 0; c < N; c++) {
        out = min(out, dp[N - 1][c]);
    }

    return out;

    // Complexity analysis
    // Time : O(N) + O(N * N) + O(N)
    // Space : O(N*N) for dp
}

int optimised(vector<vector<int>>& matrix) {
    int N = matrix.size();
    vector<int> dp(N, 0);

    // 0th row - base case
    for (int c = 0; c < N; c++) {
        dp[c] = matrix[0][c];
    }

    for (int r = 1; r < N; r++) {
        vector<int> tempo(N, 0);

        for (int c = 0; c < N; c++) {
            // directly up - for down
            tempo[c] = dp[c];

            // diagonally left
            if (c > 0 && tempo[c] > dp[c - 1]) {
                tempo[c] = dp[c - 1];
            }

            // diagonally right
            if (c < N - 1 && tempo[c] > dp[c + 1]) {
                tempo[c] = dp[c + 1];
            }

            // add current cell 
            tempo[c] += matrix[r][c];
        }

        dp = tempo;
    }

    int out = INT_MAX;
    for (int c = 0; c < N; c++) {
        out = min(out, dp[c]);
    }

    return out;

    // Complexity analysis
    // Time : O(N) + O(N * N) + O(N)
    // Space : O(2N) for state (curr and prev)
}

int minFallingPathSum(vector<vector<int>>& matrix) {
    // recursion
    // return recursion(matrix);

    // memoization
    // return memoization(matrix);

    // tabulation
    // return tabulation(matrix);

    // space optimised
    return optimised(matrix);
}

void p1() {
    // Problem 1 : Leetcode 931. Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/path-in-matrix3805/1 

    vector<vector<int>> matrix = { {2,1,3},{6,5,4},{7,8,9} };

    int sum = minFallingPathSum(matrix);
    cout << sum << endl;
}

int main() {
    // Day 10 of DP 

    p1();


    return 0;
}