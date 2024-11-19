#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int recursion(string& s, int i, int j) {
    if (i >= j) return 0;

    if (s[i] == s[j]) return recursion(s, i + 1, j - 1);

    int a = 1 + recursion(s, i + 1, j); // insert at j 
    int b = 1 + recursion(s, i, j - 1); // insert at i 

    return min(a, b);

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) 
}

int memoize(string& s, int i, int j, vector<vector<int>>& dp) {
    // base case 
    if (i >= j) return 0;

    if (dp[i][j] != -1) return dp[i][j];

    if (s[i] == s[j]) return dp[i][j] = memoize(s, i + 1, j - 1, dp);

    int a = memoize(s, i + 1, j, dp); // insert at j 
    int b = memoize(s, i, j - 1, dp); // insert at i 

    return dp[i][j] = 1 + min(a, b);

    // Complexity analysis 
    // Time : O(2*N) 
    // Space : O(N) + O(N*N) for memoization 
}

int __optimise(string& txt1, int n, string& txt2, int m) {
    // lcs wala 

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

int optimised(string& s, int N) {
    // using lcs method 
    // find lcs length and then return N - lcs 
    // keep lcs intact and add rest part again in the string in reverse order 

    string s2(s);
    reverse(s2.begin(), s2.end());

    return (N - __optimise(s, N, s2, N));
}

int minInsertions(string s) {
    int len = s.length();

    // recursion 
    // return recursion(s, 0, len - 1);

    // memoization 
    // vector<vector<int>> dp(len, vector<int>(len, -1));
    // return memoize(s, 0, len - 1, dp);

    // tabulation - optimised 
    return optimised(s, len);
}

void p1() {
    // Problem 1 : Leetcode 1312. Minimum Insertion Steps to Make a String Palindrome - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1 

    int is = minInsertions("helloeo");
    cout << is << endl;
}

int minDistance(string word1, string word2) {
    // similar to lcs 
    // find lenth of lcs 
    // keep lcs intact 
    // delete everything 

    int n = word1.length(), m = word2.length();

    // get lcs len 
    int lcs_len = __optimise(word1, n, word2, m);

    // left over part in both strings 
    int lo1 = n - lcs_len;
    int lo2 = m - lcs_len;
    return lo1 + lo2;
}

void p2() {
    // Problem 2 : Leetcode 583. Delete Operation for Two Strings - https://leetcode.com/problems/delete-operation-for-two-strings/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1 

    int id = minDistance("", "");
    cout << id << endl;
}


int main() {
    // Day 19 of DP 

    p1();

    p2();


    return 0;
}
