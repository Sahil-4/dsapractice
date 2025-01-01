#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    bool isPalindrome(string& s, int i, int j) {
        while (i < j) if (s[i++] != s[j--]) return false;
        return true;
    }

    int recursion(string& s, int i, int N) {
        if (i == N) return 0;

        int mcost = INT_MAX;

        for (int k = i; k < N; k++) {
            if (isPalindrome(s, i, k)) {
                int cost = 1 + recursion(s, k + 1, N);
                mcost = min(mcost, cost);
            }
        }

        return mcost;

        // Complexity analysis 
        // Time : O(N * N ^ N) 
        // Space : O(N) stack 
    }

    int memoize(string& s, int i, int N, vector<int>& dp) {
        if (i == N) return 0;

        if (dp[i] != -1) return dp[i];

        int mcost = INT_MAX;

        for (int k = i; k < N; k++) {
            if (!isPalindrome(s, i, k)) continue;

            int cost = 1 + memoize(s, k + 1, N, dp);
            mcost = min(mcost, cost);
        }

        return dp[i] = mcost;

        // Complexity analysis 
        // Time : O(N * N ^ N) 
        // Space : O(N) stack + O(N) memory 
    }

    int tabulation(string s, int N) {
        vector<int> dp(N + 1, 0);

        for (int i = N - 1; i >= 0; i--) {
            int mcost = INT_MAX;

            for (int k = i; k < N; k++) {
                if (!isPalindrome(s, i, k)) continue;

                int cost = 1 + dp[k + 1];
                mcost = min(mcost, cost);
            }

            dp[i] = mcost;
        }

        return dp[0] - 1;

        // Complexity analysis 
        // Time : O(N * N * N) 
        // Space : O(N) memory 
    }

public:
    int minCut(string s) {
        int N = s.length();

        // return recursion(s, 0, N) - 1;

        // vector<int> dp(N, -1);
        // return memoize(s, 0, N, dp) - 1;

        return tabulation(s, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 132. Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/ 

    cout << Problem1().minCut("aba") << endl;
    cout << Problem1().minCut("ababa") << endl;
    cout << Problem1().minCut("ababab") << endl;
    cout << Problem1().minCut("abcaa") << endl;
}

class Problem2 {
    int solve(vector<vector<int>>& matrix, int N, int M) {
        vector<vector<int>> dp(N, vector<int>(M, 0));

        // copy first row and col 
        for (int i = 0; i < N; i++) dp[i][0] = matrix[i][0]; // all rows first cols 
        for (int j = 0; j < M; j++) dp[0][j] = matrix[0][j]; // all cols first rows 

        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                int mn = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]));
                dp[i][j] = (mn + 1) * matrix[i][j];
            }
        }

        int out = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                out += dp[i][j];
            }
        }

        return out;

        // Complexity analysis 
        // Time : O(2 * N*M) 
        // Space : O(N*M) 
    }

public:
    int countSquares(int N, int M, vector<vector<int>> matrix) {
        // code here 

        return solve(matrix, N, M);
    }
};

void p2() {
    // Problem 2 : Geeksforgeeks Count Square Submatrices with All Ones - https://www.geeksforgeeks.org/problems/count-square-submatrices-with-all-ones/0 

    cout << Problem2().countSquares(3, 4, { {0, 1, 1, 1}, {1, 1, 1, 1}, {0, 1, 1, 1} }) << endl;
}


int main() {
    // Day 28 of December 

    p1();

    p2();


    return 0;
}