#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(string word1, int index1, string word2, int index2) {
        if (word1.length() == index1) return (word2.length() - index2);
        if (word2.length() == index2) return (word1.length() - index1);

        if (word1[index1] == word2[index2]) {
            return recursion(word1, index1 + 1, word2, index2 + 1);
        }
        else {
            int a = 1 + recursion(word1, index1 + 1, word2, index2);
            int b = 1 + recursion(word1, index1, word2, index2 + 1);
            return min(a, b);
        }

        // Complexity analysis 
        // Time : O(2^(N+M)) 
        // Space : O(N+M) 
    }

    int memoize(string word1, int index1, string word2, int index2, vector<vector<int>>& dp) {
        if (index1 == word1.length()) return (word2.length() - index2);
        if (index2 == word2.length()) return (word1.length() - index1);

        if (dp[index1][index2] != -1) return dp[index1][index2];

        if (word1[index1] == word2[index2]) {
            return dp[index1][index2] = memoize(word1, index1 + 1, word2, index2 + 1, dp);
        }
        else {
            int a = 1 + memoize(word1, index1 + 1, word2, index2, dp);
            int b = 1 + memoize(word1, index1, word2, index2 + 1, dp);
            return dp[index1][index2] = min(a, b);
        }

        // Complexity analysis 
        // Time : O(2*2*(N+M)) 
        // Space : O(N+M) + O(N*M) 
    }

    int tabulation(string word1, string word2) {
        int N = word1.length(), M = word2.length();
        vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));

        // base 
        for (int index2 = 0; index2 <= M; index2++) dp[N][index2] = (M - index2);
        for (int index1 = 0; index1 <= N; index1++) dp[index1][M] = (N - index1);

        // recurrence 
        for (int index1 = N - 1; index1 >= 0; index1--) {
            for (int index2 = M - 1; index2 >= 0; index2--) {
                if (word1[index1] == word2[index2]) {
                    dp[index1][index2] = dp[index1 + 1][index2 + 1];
                }
                else {
                    int a = 1 + dp[index1 + 1][index2];
                    int b = 1 + dp[index1][index2 + 1];
                    dp[index1][index2] = min(a, b);
                }

            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N+1*M+1) 
        // Space : O(N+1*M+1) 
    }

public:
    int minDistance(string word1, string word2) {
        int N = word1.length(), M = word2.length();

        // return recursion(word1, 0, word2, 0);

        // vector<vector<int>> dp(N, vector<int>(M, -1));
        // return memoize(word1, 0, word2, 0, dp);

        return tabulation(word1, word2);
    }
};

void p1() {
    // Problem 1 : Leetcode 583. Delete Operation for Two Strings - https://leetcode.com/problems/delete-operation-for-two-strings/ 

    cout << Problem1().minDistance("abc", "dcs") << endl;
    cout << Problem1().minDistance("abc", "abc") << endl;
    cout << Problem1().minDistance("abc", "def") << endl;
}

class Problem2 {
    int recursion(string& str, int l, int r) {
        if (l >= r) return 0;

        if (str[l] == str[r]) {
            return recursion(str, l + 1, r - 1);
        }
        else {
            int a = 1 + recursion(str, l + 1, r);
            int b = 1 + recursion(str, l, r - 1);
            return min(a, b);
        }
    }

    int memoize(string& str, int l, int r, vector<vector<int>>& dp) {
        if (l >= r) return 0;

        if (dp[l][r] != -1) return dp[l][r];

        if (str[l] == str[r]) {
            return dp[l][r] = memoize(str, l + 1, r - 1, dp);
        }
        else {
            int a = 1 + memoize(str, l + 1, r, dp);
            int b = 1 + memoize(str, l, r - 1, dp);
            return dp[l][r] = min(a, b);
        }
    }

    int tabulation(string str) {
        int n = str.length();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        // base - handled 

        // recurrence 
        for (int l = n - 1; l >= 0; l--) {
            for (int r = 1; r < n; r++) {
                if (l > r) continue;

                if (str[l] == str[r]) {
                    dp[l][r] = dp[l + 1][r - 1];
                }
                else {
                    int a = 1 + dp[l + 1][r];
                    int b = 1 + dp[l][r - 1];
                    dp[l][r] = min(a, b);
                }
            }
        }

        // return 
        return dp[0][n - 1];
    }

    int optimised(string str) {
        int n = str.length();
        vector<int> dpp(n + 1, 0);

        // base - handled 

        // recurrence 
        for (int l = n - 1; l >= 0; l--) {
            vector<int> dpn(n + 1, 0);

            for (int r = 1; r < n; r++) {
                if (l > r) continue;

                if (str[l] == str[r]) {
                    dpn[r] = dpp[r - 1];
                }
                else {
                    int a = 1 + dpp[r];
                    int b = 1 + dpn[r - 1];
                    dpn[r] = min(a, b);
                }
            }

            dpp = dpn;
        }

        // return 
        return dpp[n - 1];
    }

public:
    int countMin(string str) {
        // complete the function here 
        int n = str.length();

        // return recursion(str, 0, str.length()-1);

        // vector<vector<int>> dp(n, vector<int>(n, -1));
        // return memoize(str, 0, n-1, dp);

        // return tabulation(str);

        return optimised(str);
    }
};


void p2() {
    // Problem 2 : Geeksforgeeks Form a palindrome - https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1 

    cout << Problem2().countMin("abc");
    cout << Problem2().countMin("aba");
    cout << Problem2().countMin("ababaa");
    cout << Problem2().countMin("hele");
}


int main() {
    // Day 21 of December 

    p1();

    p2();


    return 0;
}