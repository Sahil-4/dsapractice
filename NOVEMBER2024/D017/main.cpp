#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Problem1 {
public:
    static int recursion(string& txt1, int ind1, string& txt2, int ind2) {
        if (ind1 < 0 || ind2 < 0) {
            return 0;
        }

        if (txt1[ind1] == txt2[ind2]) {
            // match 
            return 1 + recursion(txt1, ind1 - 1, txt2, ind2 - 1);
        }

        int b = 0, c = 0;

        // not match 
        if (ind1 != 0) b = recursion(txt1, ind1 - 1, txt2, ind2);
        if (ind2 != 0) c = recursion(txt1, ind1, txt2, ind2 - 1);

        return max(b, c);

        // Complexity analysis 
        // Time : O(2^(n*m)) 
        // Space : O(2N) for recursion stack space 
    }

    static int memoize(string& txt1, int ind1, string& txt2, int ind2, vector<vector<int>>& dp) {
        if (ind1 < 0 || ind2 < 0) {
            return 0;
        }

        if (dp[ind1][ind2] != -1) return dp[ind1][ind2];

        if (txt1[ind1] == txt2[ind2]) {
            // match 
            int a = 1 + memoize(txt1, ind1 - 1, txt2, ind2 - 1, dp);
            return dp[ind1][ind2] = a;
        }

        int b = 0, c = 0;

        // not match 
        if (ind1 != 0) b = memoize(txt1, ind1 - 1, txt2, ind2, dp);
        if (ind2 != 0) c = memoize(txt1, ind1, txt2, ind2 - 1, dp);

        return dp[ind1][ind2] = max(b, c);

        // Complexity analysis 
        // Time : O(2*(n*m)) 
        // Space : O(2*(n+m)) for recursion stack space + O(n * m) for memoization 
    }

    static int tabulation(string& txt1, int n, string& txt2, int m) {
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // base case 
        // for (int ind1 = 0; ind1 <= n; ind1++) dp[ind1][0] = 0;
        // for (int ind2 = 0; ind2 <= m; ind2++) dp[0][ind2] = 0;

        // recurrence copy 
        for (int ind1 = 1; ind1 <= n; ind1++) {
            for (int ind2 = 1; ind2 <= m; ind2++) {
                if (txt1[ind1 - 1] == txt2[ind2 - 1]) {
                    // match 
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
                }
                else {
                    // not match 
                    int b = dp[ind1 - 1][ind2];
                    int c = dp[ind1][ind2 - 1];
                    dp[ind1][ind2] = max(b, c);
                }
            }
        }

        return dp[n][m];

        // Complexity analysis 
        // Time : O(n * m) 
        // Space : O(n * m) for tabulating 
    }

    static int optimise(string& txt1, int n, string& txt2, int m) {
        vector<int> dpp(m + 1, 0);

        // base case - already taken care 

        // recurrence copy 
        for (int ind1 = 1; ind1 <= n; ind1++) {
            vector<int> dpc(m + 1, 0);

            for (int ind2 = 1; ind2 <= m; ind2++) {
                if (txt1[ind1 - 1] == txt2[ind2 - 1]) {
                    // match 
                    dpc[ind2] = 1 + dpp[ind2 - 1];
                }
                else {
                    // not match 
                    int b = dpp[ind2];
                    int c = dpc[ind2 - 1];
                    dpc[ind2] = max(b, c);
                }
            }

            dpp = dpc;
        }

        return dpp[m];

        // Complexity analysis 
        // Time : O(n * m) 
        // Space : O(2 * m) for tabulating 
    }

    static int longestCommonSubsequence(string text1, string text2) {
        int n = text1.length(), m = text2.length();

        // recursion 
        // return recursion(text1, n - 1, text2, m - 1);

        // memoization 
        // vector<vector<int>> dp(n, vector<int>(m, -1));
        // return memoize(text1, n - 1, text2, m - 1, dp);

        // tabulation 
        // return tabulation(text1, n, text2, m);

        // space optimise 
        return optimise(text1, n, text2, m);
    }
};

void p1() {
    // Problem 1 : Leetcode 1143. Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1 

    string text1 = "abscs";
    string text2 = "asc";

    int common = Problem1().longestCommonSubsequence(text1, text2);
    cout << common << endl;
}


int main() {
    // Day 17 of DP 

    p1();


    return 0;
}