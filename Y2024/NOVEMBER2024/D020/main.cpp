#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string shortestCommonSupersequence(string str1, string str2) {
    /*
        Intution
        - INPUT str1 = "abac", str2 = "cab"
        - OUTPUT "cabac"

        we know super sequence will contain both the strings str1, and str2
        but smallest super sequence will only contain common character once
        or i should say smallest super sequence will only contain lcs (longest common sub sequence) once

        lcs("abac", "cab") = ['a','b']
        ['a','b','a','c'](0,1,2,3) - ['a','b'] (0,1) => ['a','c'](2,3)
        ['c','a','b'](0,1,2) - ['a','b'] (1,2) => ['c'](0)
        so lc-super-seq will contain [['a','b'] (common), ['a','c'](2,3) (str1), ['c'](0) (str2)]
        as subsequece persists indexes we have to put characters which appered first
        [['a','b'] (common), ['a','c'](2,3) (str1), ['c'](0) (str2)]
        [['c'](0) (str2) + ['a','b'] (common), ['a','c'](2,3) (str1)]

        now we just have to find out lcs (comm subseq)
        and then find non matching chars to build lcs(comm super-seq)
    */

    // ------------ using lcs method ---------------- 

    int N = str1.length(), M = str2.length();

    vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                // common 
                dp[i][j] = 1 + dp[i - 1][j - 1];
            }
            else {
                // not common 
                int mu = dp[i - 1][j];
                int ml = dp[i][j - 1];
                dp[i][j] = max(mu, ml);
            }
        }
    }

    // now build lc-superseq 

    // ---------------- using build lcs(subseq) method ------------------ 

    string super = "";
    int rn = N, cn = M;

    while (rn > 0 && cn > 0) {
        if (str1[rn - 1] == str2[cn - 1]) {
            super += str1[rn - 1]; rn--; cn--;
        }
        else if (dp[rn - 1][cn] > dp[rn][cn - 1]) {
            super += str1[rn - 1]; rn--;
        }
        else {
            super += str2[cn - 1]; cn--;
        }
    }

    while (rn > 0) { super += str1[rn - 1]; rn--; }
    while (cn > 0) { super += str2[cn - 1]; cn--; }

    reverse(super.begin(), super.end());

    return super;

    // Complexity analysis 
    // Time : O(N+1 * M+1) + O(N + M) 
    // Space : O(N+1 * M+1) for dp table 
}

void p1() {
    // Problem 1 : Leetcode 1092. Shortest Common Supersequence - https://leetcode.com/problems/shortest-common-supersequence/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1 

    string str1 = "abac", str2 = "caba";
    string super = shortestCommonSupersequence(str1, str2);
    cout << super << endl;
}

int recursion(string& s, int i, string& t, int j) {
    if (j < 0) return 1;
    if (i < 0) return 0;

    int nm = recursion(s, i - 1, t, j);

    if (s[i] == t[j]) return nm + recursion(s, i - 1, t, j - 1);

    return nm;

    // Complexity analysis 
    // Time : O(2^(N*M)) 
    // Space : O(N + M) stack 
}

int memoize(string& s, int i, string& t, int j, vector<vector<int>>& dp) {
    if (j < 0) return 1;
    if (i < 0) return 0;

    if (dp[i][j] != -1) return dp[i][j];

    int nm = memoize(s, i - 1, t, j, dp);

    if (s[i] == t[j]) return dp[i][j] = nm + memoize(s, i - 1, t, j - 1, dp);

    return dp[i][j] = nm;

    // Complexity analysis 
    // Time : O(2*(N*M)) 
    // Space : O(N + M) stack + O(N*M) for memoize 
}

int tabulation(string& s, int N, string& t, int M) {
    vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));

    // base case 
    for (int i = 0; i <= N; i++) dp[i][0] = 1;

    // recurrence 
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            dp[i][j] = dp[i - 1][j];
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = ((long long)dp[i][j] + (long long)dp[i - 1][j - 1]);
            }
        }
    }

    // return 
    return dp[N][M];

    // Complexity analysis 
    // Time : O(N * M) 
    // Space : O(N*M) for table 
}

int optimise(string& s, int N, string& t, int M) {
    vector<int> dpp(M + 1, 0);

    // base case 
    dpp[0] = 1;

    // recurrence 
    for (int i = 1; i <= N; i++) {
        vector<int> dpc(M + 1, 0);
        dpc[0] = 1;
        for (int j = 1; j <= M; j++) {
            dpc[j] = dpp[j];
            if (s[i - 1] == t[j - 1]) {
                dpc[j] = ((long long)dpc[j] + (long long)dpp[j - 1]);
            }
        }
        dpp = dpc;
    }

    // return 
    return dpp[M];

    // Complexity analysis 
    // Time : O(N * M) 
    // Space : O(2*M) for table 
}

int numDistinct(string s, string t) {
    int N = s.length(), M = t.length();

    // recursion 
    // return recursion(s, N - 1, t, M - 1);

    // memoize 
    // vector<vector<int>> dp(N, vector<int>(M, -1));
    // return memoize(s, N - 1, t, M - 1, dp);

    // tabulation 
    // return tabulation(s, N, t, M);

    // space optimise 
    return optimise(s, N, t, M);
}

void p2() {
    // Problem 2 : Leetcode 115. Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/ 

    string s = "rabbbit", t = "rabbit";
    int ds = numDistinct(s, t);
    cout << ds << endl;
}


int main() {
    // Day 20 of DP 

    p1();

    p2();


    return 0;
}