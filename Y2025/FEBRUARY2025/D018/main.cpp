#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    bool recursion(string& t, int i, string& p, int j, string& q, int k) {
        if (j >= p.length() && k >= q.length()) return i >= t.length();

        bool opt1 = false;
        bool opt2 = false;

        if (j < p.length() && t[i] == p[j]) {
            opt1 = recursion(t, i + 1, p, j + 1, q, k);
        }
        if (k < q.length() && t[i] == q[k]) {
            opt2 = recursion(t, i + 1, p, j, q, k + 1);
        }

        return (opt1 || opt2);

        // Complexity analysis 
        // Time : O(2^Ni) 
        // Space : O(Ni) stack space 
    }

    bool memoize(string& t, int i, string& p, int j, string& q, int k, vector<vector<vector<int>>>& dp) {
        if (j >= p.length() && k >= q.length()) return i >= t.length();

        if (dp[i][j][k] != -1) return dp[i][j][k];

        bool opt1 = false;
        bool opt2 = false;

        if (j < p.length() && t[i] == p[j]) {
            opt1 = memoize(t, i + 1, p, j + 1, q, k, dp);
        }
        if (k < q.length() && t[i] == q[k]) {
            opt2 = memoize(t, i + 1, p, j, q, k + 1, dp);
        }

        return dp[i][j][k] = (opt1 || opt2);

        // Complexity analysis 
        // Time : O(2*Ni*Nj*Nk) 
        // Space : O(Ni) stack space + O(Ni*Nj*Nk) memory 
    }

    bool memoize2(string& t, string& p, int j, string& q, int k, vector<vector<vector<int>>>& dp) {
        if (j >= p.length() && k >= q.length()) return (j + k) >= t.length();

        if (dp[(j + k)][j][k] != -1) return dp[(j + k)][j][k];

        bool opt1 = false;
        bool opt2 = false;

        if (j < p.length() && t[(j + k)] == p[j]) {
            opt1 = memoize2(t, p, j + 1, q, k, dp);
        }
        if (k < q.length() && t[(j + k)] == q[k]) {
            opt2 = memoize2(t, p, j, q, k + 1, dp);
        }

        return dp[(j + k)][j][k] = (opt1 || opt2);

        // Complexity analysis 
        // Time : O(2*Ni*Nj*Nk) 
        // Space : O(Ni) stack space + O(Ni*Nj*Nk) memory 
    }

    bool memoize3(string& t, string& p, int j, string& q, int k, vector<vector<int>>& dp) {
        if (j >= p.length() && k >= q.length()) return (j + k) >= t.length();

        if (dp[j][k] != -1) return dp[j][k];

        bool opt1 = false;
        bool opt2 = false;

        if (j < p.length() && t[(j + k)] == p[j]) {
            opt1 = memoize3(t, p, j + 1, q, k, dp);
        }
        if (k < q.length() && t[(j + k)] == q[k]) {
            opt2 = memoize3(t, p, j, q, k + 1, dp);
        }

        return dp[j][k] = (opt1 || opt2);

        // Complexity analysis 
        // Time : O(2*Nj*Nk) 
        // Space : O(Ni) stack space + O(Nj*Nk) memory 
    }

    bool tabulation(string& t, string& p, string& q) {
        int Ni = t.length(), Nj = p.length(), Nk = q.length();

        vector<vector<vector<int>>> dp(Ni + 2, vector<vector<int>>(Nj + 2, vector<int>(Nk + 2, 0)));

        // base 

        // recurrence 
        for (int i = Ni; i >= 0; i--) {
            for (int j = Nj; j >= 0; j--) {
                for (int k = Nk; k >= 0; k--) {
                    if (j >= p.length() && k >= q.length()) {
                        dp[i][j][k] = i >= t.length();
                        continue;
                    }

                    bool opt1 = false, opt2 = false;

                    if (j < p.length() && t[i] == p[j]) {
                        opt1 = dp[i + 1][j + 1][k];
                    }
                    if (k < q.length() && t[i] == q[k]) {
                        opt2 = dp[i + 1][j][k + 1];
                    }

                    dp[i][j][k] = (opt1 || opt2);
                }
            }
        }

        // return 
        return dp[0][0][0];

        // Complexity analysis 
        // Time : O(Ni*Nj*Nk) 
        // Space : O(Ni*Nj*Nk) memory 
    }

    bool optimised(string& t, string& p, string& q) {
        int Ni = t.length(), Nj = p.length(), Nk = q.length();

        vector<vector<int>> next(Nj + 2, vector<int>(Nk + 2, 0));

        // base - handled 

        // recurrence 
        for (int i = Ni; i >= 0; i--) {
            vector<vector<int>> curr(Nj + 2, vector<int>(Nk + 2, 0));

            for (int j = Nj; j >= 0; j--) {
                for (int k = Nk; k >= 0; k--) {
                    if (j >= p.length() && k >= q.length()) {
                        curr[j][k] = i >= t.length();
                        continue;
                    }

                    bool opt1 = false, opt2 = false;

                    if (j < p.length() && t[i] == p[j]) {
                        opt1 = next[j + 1][k];
                    }
                    if (k < q.length() && t[i] == q[k]) {
                        opt2 = next[j][k + 1];
                    }

                    curr[j][k] = (opt1 || opt2);
                }
            }

            next = curr;
        }

        // return 
        return next[0][0];

        // Complexity analysis 
        // Time : O(Nj*Nk) 
        // Space : O(Ni*Nj*Nk) memory 
    }

    bool optimised2(string& t, string& p, string& q) {
        int Ni = t.length(), Nj = p.length(), Nk = q.length();

        vector<vector<int>> dp(Nj + 2, vector<int>(Nk + 2, 0));

        // base - handled 

        // recurrence 

        for (int j = Nj; j >= 0; j--) {
            for (int k = Nk; k >= 0; k--) {
                if (j >= p.length() && k >= q.length()) {
                    dp[j][k] = (j + k) >= t.length();
                    continue;
                }

                bool opt1 = false, opt2 = false;

                if (j < Nj && j + k < Ni && t[(j + k)] == p[j]) {
                    opt1 = dp[j + 1][k];
                }
                if (k < Nk && j + k < Ni && t[(j + k)] == q[k]) {
                    opt2 = dp[j][k + 1];
                }

                dp[j][k] = (opt1 || opt2);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(Nj*Nk) 
        // Space : O(Nj*Nk) memory 
    }

    bool optimised3(string& t, string& p, string& q) {
        int Ni = t.length(), Nj = p.length(), Nk = q.length();

        vector<int> next(Nk + 2, 0);

        // base - handled 

        // recurrence 

        for (int j = Nj; j >= 0; j--) {
            vector<int> curr(Nk + 2, 0);

            for (int k = Nk; k >= 0; k--) {
                if (j >= p.length() && k >= q.length()) {
                    curr[k] = (j + k) >= t.length();
                    continue;
                }

                bool opt1 = false, opt2 = false;

                if (j < Nj && j + k < Ni && t[(j + k)] == p[j]) {
                    opt1 = next[k];
                }
                if (k < Nk && j + k < Ni && t[(j + k)] == q[k]) {
                    opt2 = curr[k + 1];
                }

                curr[k] = (opt1 || opt2);
            }

            next = curr;
        }

        // return 
        return next[0];

        // Complexity analysis 
        // Time : O(Nj*Nk) 
        // Space : O(Nk) memory 
    }

public:
    bool isInterleave(string s1, string s2, string s3) {
        // return recursion(s3, 0, s1, 0, s2, 0);

        // int Ni = s3.length(), Nj = s1.length(), Nk = s2.length();
        // vector<vector<vector<int>>> dp(Ni+1, vector<vector<int>>(Nj+1, vector<int>(Nk+1, -1)));
        // return memoize(s3, 0, s1, 0, s2, 0, dp);

        // return memoize2(s3, s1, 0, s2, 0, dp);

        // int Nj = s1.length(), Nk = s2.length();
        // vector<vector<int>> dp(Nj+1, vector<int>(Nk+1, -1));
        // return memoize3(s3, s1, 0, s2, 0, dp);

        // return tabulation(s3, s1, s2);

        // return optimised(s3, s1, s2);

        // return optimised2(s3, s1, s2);

        return optimised3(s3, s1, s2);
    }
};

void p1() {
    // Problem 1 : Leetcode 97. Interleaving String - https://leetcode.com/problems/interleaving-string/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/interleaved-strings/1 

    cout << Problem1().isInterleave("abc", "def", "adbcef") << endl;
    cout << Problem1().isInterleave("abx", "def", "adbcef") << endl;
    cout << Problem1().isInterleave("xyz", "", "xyz") << endl;
    cout << Problem1().isInterleave("xyz", "w", "wxyz") << endl;
    cout << Problem1().isInterleave("xyz", "w", "xyw") << endl;
}

class Problem2 {
    int recursion(string& s, int i, string& t, int j) {
        if (i == s.length()) return (t.length() - j);
        if (j == t.length()) return (s.length() - i);

        int out = 0;

        if (s[i] == t[j]) {
            // matching chars 
            out = recursion(s, i + 1, t, j + 1);
        }
        else {
            int opt1 = recursion(s, i, t, j + 1); // insert 
            int opt2 = recursion(s, i + 1, t, j); // delete 
            int opt3 = recursion(s, i + 1, t, j + 1); // replace 
            out = 1 + min({ opt1, opt2, opt3 });
        }

        return out;

        // Complexity analysis 
        // Time : O(3^(N+M)) 
        // Space : O(N+M) stack space 
    }

    int memoize(string& s, int i, string& t, int j, vector<vector<int>>& dp) {
        if (i == s.length()) return (t.length() - j);
        if (j == t.length()) return (s.length() - i);

        if (dp[i][j] != -1) return dp[i][j];

        int out = 0;

        if (s[i] == t[j]) {
            // matching chars 
            out = memoize(s, i + 1, t, j + 1, dp);
        }
        else {
            int opt1 = memoize(s, i, t, j + 1, dp); // insert 
            int opt2 = memoize(s, i + 1, t, j, dp); // delete 
            int opt3 = memoize(s, i + 1, t, j + 1, dp); // replace 
            out = 1 + min({ opt1, opt2, opt3 });
        }

        return dp[i][j] = out;

        // Complexity analysis 
        // Time : O(2*(N*M)) 
        // Space : O(N+M) stack space + O(N*M) memory 
    }

    int tabulation(string& s, string& t) {
        int N = s.length(), M = t.length();
        vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));

        // base 
        for (int i = 0; i <= N; i++) dp[i][M] = (N - i);
        for (int j = 0; j <= M; j++) dp[N][j] = (M - j);

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            for (int j = M - 1; j >= 0; j--) {
                int out = 0;
                if (s[i] == t[j]) {
                    // matching chars 
                    out = dp[i + 1][j + 1];
                }
                else {
                    int opt1 = dp[i][j + 1]; // insert 
                    int opt2 = dp[i + 1][j]; // delete 
                    int opt3 = dp[i + 1][j + 1]; // replace 
                    out = 1 + min({ opt1, opt2, opt3 });
                }

                dp[i][j] = out;
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) memory 
    }

    int optimised(string& s, string& t) {
        int N = s.length(), M = t.length();
        vector<int> next(M + 1, 0);

        // base 
        for (int j = 0; j <= M; j++) next[j] = (M - j);

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            vector<int> curr(M + 1, 0);
            curr[M] = (N - i); // base 

            for (int j = M - 1; j >= 0; j--) {
                int out = 0;
                if (s[i] == t[j]) {
                    // matching chars 
                    out = next[j + 1];
                }
                else {
                    int opt1 = curr[j + 1]; // insert 
                    int opt2 = next[j]; // delete 
                    int opt3 = next[j + 1]; // replace 
                    out = 1 + min({ opt1, opt2, opt3 });
                }

                curr[j] = out;
            }

            next = curr;
        }

        // return 
        return next[0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(2*M) memory 
    }

public:
    int minDistance(string word1, string word2) {
        // return recursion(word1, 0, word2, 0);

        // int N = word1.length(), M = word2.length();
        // vector<vector<int>> dp(N, vector<int>(M, -1));
        // return memoize(word1, 0, word2, 0, dp);

        // return tabulation(word1, word2);

        return optimised(word1, word2);
    }
};

void p2() {
    // Problem 2 : Leetcode 72. Edit Distance - https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/edit-distance3702/1 

    cout << Problem2().minDistance("hell", "help") << endl;
    cout << Problem2().minDistance("abc", "xyz") << endl;
    cout << Problem2().minDistance("abcd", "xyz") << endl;
    cout << Problem2().minDistance("abc", "wxyz") << endl;
    cout << Problem2().minDistance("abc", "abc") << endl;
    cout << Problem2().minDistance("abc", "abcd") << endl;
    cout << Problem2().minDistance("abcd", "abc") << endl;
}


int main() {
    // Day 18 of February 

    p1();

    p2();


    return 0;
}