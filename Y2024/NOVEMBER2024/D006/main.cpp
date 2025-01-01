#include <iostream>
#include <vector>

using namespace std;

int recursion(vector<vector<int>>& arr, int N, int index, int prev) {
    if (index >= N) return 0;
    int rec1 = 0, rec2 = 0, rec3 = 0;

    if (prev != 0) rec1 = arr[index][0] + recursion(arr, N, index + 1, 0);
    if (prev != 1) rec2 = arr[index][1] + recursion(arr, N, index + 1, 1);
    if (prev != 2) rec3 = arr[index][2] + recursion(arr, N, index + 1, 2);

    return max(max(rec1, rec2), rec3);
}

int memoization(vector<vector<int>>& arr, int N, int index, int prev, vector<vector<int>>& dp) {
    if (index >= N) return 0;
    int rec1 = 0, rec2 = 0, rec3 = 0;

    if (dp[index][prev] != -1) {
        return dp[index][prev];
    }

    if (prev != 0) rec1 = arr[index][0] + memoization(arr, N, index + 1, 0, dp);
    if (prev != 1) rec2 = arr[index][1] + memoization(arr, N, index + 1, 1, dp);
    if (prev != 2) rec3 = arr[index][2] + memoization(arr, N, index + 1, 2, dp);

    return dp[index][prev] = max(max(rec1, rec2), rec3);

    // Complexity analysis 
    // Time : O(3N) approx 
    // Space : O(4N) for dp + O(N) for recursion stack 
}

int tabulation(vector<vector<int>>& arr, int N, vector<vector<int>>& dp) {
    // base case 
    dp[0][0] = max(arr[0][1], arr[0][2]);
    dp[0][1] = max(arr[0][0], arr[0][2]);
    dp[0][2] = max(arr[0][0], arr[0][1]);
    dp[0][3] = max(max(arr[0][0], arr[0][1]), arr[0][2]);

    for (int day = 1; day < N; day++) {
        for (int last = 0; last < 4; last++) {
            for (int task = 0; task < 3; task++) {
                if (task == last) continue;
                int t = arr[day][task] + dp[day - 1][task];
                dp[day][last] = max(dp[day][last], t);
            }
        }
    }

    return dp[N - 1][3];

    // Complexity analysis 
    // Time : O(N * 4 * 3) loop 
    // Space : O(4N) for dp 
}

int optimization(vector<vector<int>>& arr, int N) {
    // base case 
    vector<int> prev(4, 0);

    prev[0] = max(arr[0][1], arr[0][2]);
    prev[1] = max(arr[0][0], arr[0][2]);
    prev[2] = max(arr[0][0], arr[0][1]);
    prev[3] = max(max(arr[0][0], arr[0][1]), arr[0][2]);

    for (int day = 1; day < N; day++) {
        vector<int> temp(4, 0);

        for (int last = 0; last < 4; last++) {
            for (int task = 0; task < 3; task++) {
                if (task == last) continue;

                int t = arr[day][task] + prev[task];
                temp[last] = max(temp[last], t);
            }
        }

        prev = temp;
    }

    return prev[3];

    // Complexity analysis 
    // Time : O(N * 4 * 3) loop 
    // Space : O(2*4) for prev and current state 
}

int maximumPoints(vector<vector<int>>& arr, int n) {
    // Code here
    // recursion 
    // return recursion(arr, n, 0, -1);

    // memoization 
    // vector<vector<int>> dp(n, vector<int>(4, -1));
    // return memoization(arr, n, 0, 3, dp);

    // tabulation 
    // vector<vector<int>> dp(n, vector<int>(4, 0));
    // return tabulation(arr, n, dp);

    // space optimization 
    return optimization(arr, n);
}

void p1() {
    // Problem 1 : Geeksforgeeks Geek's Training - 
    // https://www.geeksforgeeks.org/problems/geeks-training/1 

    vector<vector<int>> arr = { {1,2,5},{3,1,1},{3,3,3} };
    int N = 3;

    int ps = maximumPoints(arr, N);
    cout << ps << endl;
}

int recursion(int row, int col, int maxRows, int maxCols) {
    if (row == maxRows - 1 && col == maxCols - 1) return 1;
    if (row > maxRows || col > maxCols) return 0;

    int c1 = recursion(row + 1, col, maxRows, maxCols);
    int c2 = recursion(row, col + 1, maxRows, maxCols);

    return c1 + c2;
}

int memoization(int row, int col, int maxRows, int maxCols, vector<vector<int>>& dp) {
    if (row == maxRows - 1 && col == maxCols - 1) return 1;
    if (row > maxRows || col > maxCols) return 0;

    if (dp[row][col] != -1) return dp[row][col];

    int c1 = memoization(row + 1, col, maxRows, maxCols, dp);
    int c2 = memoization(row, col + 1, maxRows, maxCols, dp);

    return dp[row][col] = (c1 + c2);

    // Complexity analysis 
    // Time : O(m + n) 
    // Space : O(m * n) for dp + O(m + n) for recursion stack 
}

int getAdjacent(vector<vector<int>>& dp, int i, int j) {
    if (i < 0 || i >= dp.size() || j < 0 || j >= dp[0].size()) return 0;
    return dp[i][j];
}

int tabulation(int m, int n, vector<vector<int>>& dp) {
    dp[0][0] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;

            int top = getAdjacent(dp, i - 1, j);
            int left = getAdjacent(dp, i, j - 1);
            dp[i][j] = top + left;
        }
    }

    return dp[m - 1][n - 1];

    // Complexity analysis 
    // Time : O(m * n) 
    // Space : O(m * n) 
}

int uniquePaths(int m, int n) {
    // recursion
    // return recursion(0, 0, m, n);

    // memoization
    // vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
    // return memoization(0, 0, m, n, dp);

    // tabulation 
    vector<vector<int>> dp(m, vector<int>(n, 0));
    return tabulation(m, n, dp);
}

void p2() {
    // Problem 2 : Leetcode 62. Unique Paths - 
    // https://leetcode.com/problems/unique-paths/ 

    cout << uniquePaths(3, 2) << endl;
}


int main() {
    // Day 6 of DP 

    p1();

    p2();


    return 0;
}