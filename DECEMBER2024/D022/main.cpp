#include <bits/stdc++.h>

using namespace std;


string shortestCommonSupersequence(string str1, string str2) {
    int N = str1.length(), M = str2.length();
    vector<vector<int>> lcs_len_dp(N + 1, vector<int>(M + 1, 0));

    // get the length of longest common subseq at different indexes 

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                lcs_len_dp[i][j] = 1 + lcs_len_dp[i - 1][j - 1];
            } else {
                int a = lcs_len_dp[i - 1][j];
                int b = lcs_len_dp[i][j - 1];
                lcs_len_dp[i][j] = max(a, b);
            }
        }
    }

    // get the longest common superseq 

    string superseq = "";
    int r = N, c = M;

    while (r > 0 && c > 0) {
        if (str1[r - 1] == str2[c - 1]) {
            superseq += str1[r - 1];
            r--, c--;
        } else if (lcs_len_dp[r - 1][c] > lcs_len_dp[r][c - 1]) {
            superseq += str1[--r];
        } else {
            superseq += str2[--c];
        }
    }

    while (r > 0) superseq += str1[--r];
    while (c > 0) superseq += str2[--c];

    reverse(superseq.begin(), superseq.end());

    return superseq;
}

void p1() {
    // Problem 1 : Leetcode 1092. Shortest Common Supersequence - https://leetcode.com/problems/shortest-common-supersequence/ 

    cout << shortestCommonSupersequence("abc", "daba") << endl;
    cout << shortestCommonSupersequence("abc", "abc") << endl;
    cout << shortestCommonSupersequence("abc", "abcded") << endl;
    cout << shortestCommonSupersequence("dedabc", "abc") << endl;
}

bool recursion(string& txt, int index1, string& pat, int index2) {
    if (index1 == txt.length() && index2 == pat.length()) return true;
    if (index1 < txt.length() && index2 == pat.length()) return false;
    if (index1 == txt.length() && index2 < pat.length()) {
        while (index2 < pat.length()) {
            if (pat[index2++] != '*') return false;
        }
        return true;
    }

    if (pat[index2] == '*') {
        // int a = recursion(txt, index1, pat, index2);
        bool a = recursion(txt, index1, pat, index2 + 1);
        bool b = recursion(txt, index1 + 1, pat, index2);
        return a || b;
    } else if (pat[index2] == '?' || pat[index2] == txt[index1]) {
        return recursion(txt, index1 + 1, pat, index2 + 1);
    } else {
        return false;
    }
}

bool memoize(string& txt, int index1, string& pat, int index2, vector<vector<int>>& dp) {
    if (index1 == txt.length() && index2 == pat.length()) return true;
    if (index1 < txt.length() && index2 == pat.length()) return false;
    if (index1 == txt.length() && index2 < pat.length()) {
        while (index2 < pat.length()) {
            if (pat[index2++] != '*') return false;
        }
        return true;
    }

    if (dp[index1][index2] != -1) return dp[index1][index2];

    bool out = false;

    if (pat[index2] == '*') {
        bool a = memoize(txt, index1, pat, index2 + 1, dp);
        bool b = memoize(txt, index1 + 1, pat, index2, dp);
        out = a || b;
    } else if (pat[index2] == '?' || pat[index2] == txt[index1]) {
        out = memoize(txt, index1 + 1, pat, index2 + 1, dp);
    } else {
        out = false;
    }

    return dp[index1][index2] = out;
}

bool tabulation(string& txt, string& pat) {
    int N = txt.length(), M = pat.length();

    vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));

    dp[N][M] = 1;
    for (int index2 = 0; index2 < M; index2++) {
        dp[N][index2] = true;
        for (int in2 = index2; in2 < M; in2++) {
            if (pat[in2] != '*') {
                dp[N][index2] = false;
                break;
            }
        }
    }

    for (int index1 = N - 1; index1 >= 0; index1--) {
        for (int index2 = M - 1; index2 >= 0; index2--) {
            bool out = false;
            if (pat[index2] == '*') {
                bool a = dp[index1][index2 + 1];
                bool b = dp[index1 + 1][index2];
                out = a || b;
            } else if (pat[index2] == '?' || pat[index2] == txt[index1]) {
                out = dp[index1 + 1][index2 + 1];
            } else {
                out = false;
            }
            dp[index1][index2] = out;
        }
    }

    return dp[0][0];
}

/*You are required to complete this method*/
bool wildCard(string txt, string pat) {
    // code here
    // int N = txt.length(), M = pat.length();

    // return recursion(txt, 0, pat, 0);

    // vector<vector<int>> dp(N, vector<int>(M, -1));
    // return memoize(txt, 0, pat, 0, dp);

    return tabulation(txt, pat);
}

void p2() {
    // Problem 2 : Geeksforgeeks Wildcard Pattern Matching - https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1 

    cout << wildCard("alpha", "al?*a") << endl;
    cout << wildCard("alpha", "al?*ha") << endl;
    cout << wildCard("alpha", "al?*") << endl;
}


int main() {
    // Day 22 of December 

    p1();

    p2();


    return 0;
}