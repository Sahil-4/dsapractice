#include <iostream>
#include <string>
#include <vector>

using namespace std;

int recursion(string& word1, int i, string& word2, int j) {
    if (i < 0) return j + 1;
    if (j < 0) return i + 1;

    if (word1[i] == word2[j]) return recursion(word1, i - 1, word2, j - 1);

    int ins = recursion(word1, i, word2, j - 1);
    int del = recursion(word1, i - 1, word2, j);
    int rep = recursion(word1, i - 1, word2, j - 1);

    int out = 1 + min(min(ins, del), rep);

    return out;

    // Complexity analysis 
    // Time : O(3^(n*m)) 
    // Space : O(n + m) stack space 
}

int memoization(string& word1, int i, string& word2, int j, vector<vector<int>>& dp) {
    if (i < 0) return j + 1;
    if (j < 0) return i + 1;

    if (dp[i][j] != -1) return dp[i][j];

    if (word1[i] == word2[j]) return dp[i][j] = memoization(word1, i - 1, word2, j - 1, dp);

    int ins = memoization(word1, i, word2, j - 1, dp);
    int del = memoization(word1, i - 1, word2, j, dp);
    int rep = memoization(word1, i - 1, word2, j - 1, dp);

    int out = 1 + min(min(ins, del), rep);

    return dp[i][j] = out;

    // Complexity analysis 
    // Time : O(3*(n*m)) 
    // Space : O(n*m) stack space + O(n*m) for memoization 
}

int tabulation(string& word1, int n, string& word2, int m) {
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    // base 
    // for i = 0
    for (int j = 0; j <= m; j++) dp[0][j] = j;
    // for j = 0
    for (int i = 0; i <= n; i++) dp[i][0] = i;

    // recurre
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else {
                int ins = dp[i][j - 1];
                int del = dp[i - 1][j];
                int rep = dp[i - 1][j - 1];
                dp[i][j] = 1 + min(min(ins, del), rep);;
            }
        }
    }

    // return 
    return dp[n][m];

    // Complexity analysis 
    // Time : O(n+1*m+1) 
    // Space : O(n+1*m+1) for tabulation 
}

int optimise(string& word1, int n, string& word2, int m) {
    vector<int> dpp(m + 1, 0);

    // base 
    for (int j = 0; j <= m; j++) dpp[j] = j;

    // recurre
    for (int i = 1; i <= n; i++) {
        vector<int> dpc(m + 1, 0);
        dpc[0] = i;

        for (int j = 1; j <= m; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                dpc[j] = dpp[j - 1];
            }
            else {
                int ins = dpc[j - 1];
                int del = dpp[j];
                int rep = dpp[j - 1];
                dpc[j] = 1 + min(min(ins, del), rep);;
            }
        }

        dpp = dpc;
    }

    // return 
    return dpp[m];

    // Complexity analysis 
    // Time : O(n+1*m+1) 
    // Space : O(2*m+1) for tabulation 
}

int minDistance(string word1, string word2) {
    int n = word1.length(), m = word2.length();

    // recursion 
    // return recursion(word1, n - 1, word2, m - 1);

    // memoization 
    // vector<vector<int>> dp(n, vector<int>(m, -1));
    // return memoization(word1, n - 1, word2, m - 1, dp);

    // tabulation 
    // return tabulation(word1, n, word2, m);

    // space optimise 
    return optimise(word1, n, word2, m);
}

void p1() {
    // Problem 1 : Leetcode 72. Edit Distance - https://leetcode.com/problems/edit-distance/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/edit-distance3702/1 

    string word1 = "ran", word2 = "dom";
    int d = minDistance(word1, word2);
    cout << d << endl;
}

bool __recursion(string& s, int i, string& p, int j) {
    if (i < 0 && j < 0) return true;
    if (i >= 0 && j < 0) return false;
    if (i < 0 && j >= 0) {
        while (j >= 0) {
            if (p[j--] != '*') return false;
        }
        return true;
    }

    if ((s[i] == p[j]) || (p[j] == '?')) return __recursion(s, i - 1, p, j - 1);

    if (p[j] != '*') return false;

    // match 0 
    bool c1 = __recursion(s, i, p, j - 1);
    if (c1) return true;

    // match 1 or more 
    bool c2 = __recursion(s, i - 1, p, j);
    return c2;

    // Complexity analysis 
    // Time : O(2^(N*M)) 
    // Space : O(N+M) stack space 
}

int __memoization(string& s, int i, string& p, int j, vector<vector<int>>& dp) {
    if (i < 0 && j < 0) return 1;
    if (i >= 0 && j < 0) return 0;
    if (i < 0 && j >= 0) {
        while (j >= 0) {
            if (p[j--] != '*') return 0;
        }
        return 1;
    }

    if (dp[i][j] != -1) return dp[i][j];

    if ((s[i] == p[j]) || (p[j] == '?')) return dp[i][j] = __memoization(s, i - 1, p, j - 1, dp);

    if (p[j] != '*') return dp[i][j] = 0;

    // match 0 
    int c1 = __memoization(s, i, p, j - 1, dp);
    if (c1) return dp[i][j] = 1;

    // match 1 or more 
    int c2 = __memoization(s, i - 1, p, j, dp);
    return dp[i][j] = c2;

    // Complexity analysis 
    // Time : O(2*(N*M)) 
    // Space : O(N+M) stack space + O(N*M) memory 
}

bool __tabulation(string& s, int N, string& p, int M) {
    vector<vector<bool>> dp(N + 1, vector<bool>(M + 1, false));

    // base cases 
    dp[0][0] = true;
    for (int i = 1; i <= N; i++) dp[i][0] = false;
    for (int j = 1; j <= M; j++) {
        bool flag = true;
        for (int jj = 1; jj <= j; jj++) {
            if (p[jj - 1] != '*') { flag = false; break; }
        }
        dp[0][j] = flag;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else if (p[j - 1] != '*') {
                dp[i][j] = false;
            }
            else {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            }
        }
    }

    return dp[N][M];

    // Complexity analysis 
    // Time : O(N+1*M+1) 
    // Space : O(N+1*M+1) memory 
}

bool __optimise(string& s, int N, string& p, int M) {
    vector<bool> dpp(M + 1, false);

    // base cases 
    dpp[0] = true;
    // for (int i = 1; i <= N; i++) dp[i][0] = false;
    for (int j = 1; j <= M; j++) {
        bool flag = true;
        for (int jj = 1; jj <= j; jj++) {
            if (p[jj - 1] != '*') { flag = false; break; }
        }
        dpp[j] = flag;
    }

    for (int i = 1; i <= N; i++) {
        vector<bool> dpc(M + 1, false);

        for (int j = 1; j <= M; j++) {
            if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                dpc[j] = dpp[j - 1];
            }
            else if (p[j - 1] != '*') {
                dpc[j] = false;
            }
            else {
                dpc[j] = dpc[j - 1] || dpp[j];
            }
        }

        dpp = dpc;
    }

    return dpp[M];

    // Complexity analysis 
    // Time : O(N+1*M+1) 
    // Space : O(2*M+1) memory 
}

bool isMatch(string s, string p) {
    int N = s.length(), M = p.length();

    // recursion 
    // return __recursion(s, N-1, p, M-1);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(M, -1));
    // return __memoization(s, N-1, p, M-1, dp) == 1 ? true : false;

    // tabulation 
    // return __tabulation(s, N, p, M);

    // space optimise 
    return __optimise(s, N, p, M);
}

void p2() {
    // Problem 2 : Leetcode 44. Wildcard Matching - https://leetcode.com/problems/wildcard-matching/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1 

    string s = "aaaababbbaaabaabbbbabaababaabbabbaabababbaaaaaaabba";
    string p = "baaaaba*****b***ab******";
    bool check = isMatch(s, p);
    cout << check << endl;
}


int main() {
    // Day 21 of DP 

    p1();

    p2();


    return 0;
}