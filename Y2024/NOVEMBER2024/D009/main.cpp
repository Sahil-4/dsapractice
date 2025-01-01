#include <iostream>
#include <vector>

using namespace std;

int recursion(vector<vector<int>>& triangle, int r, int c) {
    // base case - index goes out of triangle
    if (r >= triangle.size() || c >= triangle[r].size()) return 0;

    int adj1 = recursion(triangle, r + 1, c);
    int adj2 = recursion(triangle, r + 1, c + 1);

    return triangle[r][c] + min(adj1, adj2);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) for recursion stack space
}

int memoization(vector<vector<int>>& triangle, int r, int c, vector<vector<int>>& dp) {
    // base case - index goes out of triangle
    if (r >= triangle.size() || c >= triangle[r].size()) return 0;

    if (dp[r][c] != -1) return dp[r][c];

    int adj1 = memoization(triangle, r + 1, c, dp);
    int adj2 = memoization(triangle, r + 1, c + 1, dp);

    return dp[r][c] = (triangle[r][c] + min(adj1, adj2));

    // Complexity analysis
    // Time : O(N^2)
    // Space : O(N) for recursion stack space + O(N^2) for dp
}

int getDP(vector<vector<int>>& dp, int r, int c) {
    if (r < 0 || r >= dp.size() || (c < 0 || c > r)) return 0;
    return dp[r][c];
}

int tabulation(vector<vector<int>>& triangle, vector<vector<int>>& dp) {
    int N = triangle.size();

    for (int r = N - 1; r >= 0; r--) {
        for (int c = r; c >= 0; c--) {
            int adj1 = getDP(dp, r + 1, c);
            int adj2 = getDP(dp, r + 1, c + 1);

            dp[r][c] = triangle[r][c] + min(adj1, adj2);
        }
    }

    return dp[0][0];

    // Complexity analysis
    // Time : O(N^2)
    // Space : O(N^2) for dp
}

int getDP(vector<int>& dp, int r, int c) {
    if (r < 0 || r >= dp.size() || (c < 0 || c > r)) return 0;
    return dp[c];
}

int optimised(vector<vector<int>>& triangle) {
    int N = triangle.size();

    vector<int> dp(N, 0);

    for (int r = N - 1; r >= 0; r--) {
        vector<int> tempo(N, 0);
        for (int c = r; c >= 0; c--) {
            int adj1 = getDP(dp, r + 1, c);
            int adj2 = getDP(dp, r + 1, c + 1);

            tempo[c] = triangle[r][c] + min(adj1, adj2);
        }

        dp = tempo;
    }

    return dp[0];

    // Complexity analysis
    // Time : O(N^2)
    // Space : O(2N) for dp
}

int minimumTotal(vector<vector<int>>& triangle) {
    int N = triangle.size();

    // recursion
    // return recursion(triangle, 0, 0);

    // tabulation
    // vector<vector<int>> dp(N, vector<int>(N, -1));
    // return memoization(triangle, 0, 0, dp);

    // tabulation
    // vector<vector<int>> dp(N, vector<int>(N, 0));
    // return tabulation(triangle, dp);

    // space optimised
    return optimised(triangle);
}

void p1() {
    // Problem 1 : Leetcode 120. Triangle - https://leetcode.com/problems/triangle/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/triangle-path-sum/1 

    vector<vector<int>> triangle = {
                            {2},
                            {3, 4},
                            {6, 5, 7},
                            {4, 1, 8, 3},
    };

    int sum = minimumTotal(triangle);
    cout << sum << endl;
}


int main() {
    // Day 9 of DP 

    p1();


    return 0;
}