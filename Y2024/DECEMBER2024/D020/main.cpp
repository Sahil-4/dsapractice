#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(string text1, int index1, string text2, int index2) {
        // base 
        if (index1 == text1.length()) return 0;
        if (index2 == text2.length()) return 0;

        // recursion 
        int not_same1 = recursion(text1, index1 + 1, text2, index2);
        int not_same2 = recursion(text1, index1, text2, index2 + 1);
        int same = 0;
        if (text1[index1] == text2[index2]) same = 1 + recursion(text1, index1 + 1, text2, index2 + 1);

        // return 
        return max(max(not_same1, not_same2), same);

        // Complexity analysis 
        // Time : O(3^(N+M)) 
        // Space : O(N+M) 
    }

    int memoize(string text1, int index1, string text2, int index2, vector<vector<int>>& dp) {
        // base 
        if (index1 == text1.length()) return 0;
        if (index2 == text2.length()) return 0;

        if (dp[index1][index2] != -1) return dp[index1][index2];

        // recursion 
        int not_same1 = memoize(text1, index1 + 1, text2, index2, dp);
        int not_same2 = memoize(text1, index1, text2, index2 + 1, dp);
        int same = 0;
        if (text1[index1] == text2[index2]) same = 1 + memoize(text1, index1 + 1, text2, index2 + 1, dp);

        // return 
        return dp[index1][index2] = max(max(not_same1, not_same2), same);

        // Complexity analysis 
        // Time : O(3*3*(N+M)) 
        // Space : O(N+M) + O(N*M) 
    }

    int tabulation(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, 0));

        // base case - handled dp[N][...] = 0, dp[...][N] = 0  

        // recurrence 
        for (int index1 = text1.size() - 1; index1 >= 0; index1--) {
            for (int index2 = text2.size() - 1; index2 >= 0; index2--) {
                // recursion 
                int not_same1 = dp[index1 + 1][index2];
                int not_same2 = dp[index1][index2 + 1];
                int same = 0;
                if (text1[index1] == text2[index2]) same = 1 + dp[index1 + 1][index2 + 1];
                dp[index1][index2] = max(max(not_same1, not_same2), same);

            }
        }

        for (vector<int> v : dp) {
            for (int e : v) cout << e << " ";
            cout << endl;
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) 
    }

    int optimised(string text1, string text2) {
        // vector<vector<int>> dp(text1.size()+1, vector<int>(text2.size()+1, 0));
        vector<int> dpp(text2.size() + 1, 0);

        // recurrence 
        for (int index1 = text1.size() - 1; index1 >= 0; index1--) {
            vector<int> dpn(text2.size() + 1, 0);

            for (int index2 = text2.size() - 1; index2 >= 0; index2--) {
                // recursion 
                int not_same1 = dpp[index2];
                int not_same2 = dpn[index2 + 1];
                int same = 0;
                if (text1[index1] == text2[index2]) same = 1 + dpp[index2 + 1];
                dpn[index2] = max(max(not_same1, not_same2), same);

            }

            dpp = dpn;
        }

        // return 
        return dpp[0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(2*M) 
    }

    int print_lcs(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, 0));

        // base case - handled dp[N][...] = 0, dp[...][N] = 0  

        // recurrence 
        for (int index1 = text1.size() - 1; index1 >= 0; index1--) {
            for (int index2 = text2.size() - 1; index2 >= 0; index2--) {
                // recursion 
                int not_same1 = dp[index1 + 1][index2];
                int not_same2 = dp[index1][index2 + 1];
                int same = 0;
                if (text1[index1] == text2[index2]) same = 1 + dp[index1 + 1][index2 + 1];
                dp[index1][index2] = max(max(not_same1, not_same2), same);

            }
        }

        // print lcs 
        string lcs = "";
        int index1 = 0, index2 = 0;
        while (index1 < text1.length() && index2 < text2.length()) {
            if (dp[index1][index2] == 0) break;

            if (text1[index1] == text2[index2]) {
                lcs = lcs + text1[index1];
                index1++, index2++;
            } else {
                if (dp[index1 + 1][index2] > dp[index1][index2 + 1]) index1++;
                else index2++;
            }
        }
        cout << lcs << endl;

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) 
    }

public:
    int longestCommonSubsequence(string text1, string text2) {
        // return recursion(text1, 0, text2, 0);

        // vector<vector<int>> dp(text1.size(), vector<int>(text2.size(), -1));
        // return memoize(text1, 0, text2, 0, dp);

        // return tabulation(text1, text2);

        return optimised(text1, text2);

        // return print_lcs(text1, text2);
    }
};


void p1() {
    // Problem 1 : Leetcode 1143. Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1 

    cout << Problem1().longestCommonSubsequence("acddcab", "abc");
}


int main() {
    // Day 20 of December 

    p1();


    return 0;
}