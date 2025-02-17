#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int MODO = INT_MAX;

    int recursion(vector<vector<int>>& grid, int i = 0, int j = 0) {
        if (i > grid.size() - 1 || j > grid[0].size() - 1 || grid[i][j] == 1) return 0;
        if (i == grid.size() - 1 && j == grid[0].size() - 1) return 1;

        int down = recursion(grid, i + 1, j);
        int right = recursion(grid, i, j + 1);

        return (down + right);

        // Complexity analysis 
        // Time : O(2^(N+M)) 
        // Space : O(N+M) stack 
    }

    int memoize(vector<vector<int>>& grid, vector<vector<int>>& dp, int i = 0, int j = 0) {
        if (i > grid.size() - 1 || j > grid[0].size() - 1 || grid[i][j] == 1) return 0;
        if (i == grid.size() - 1 && j == grid[0].size() - 1) return 1;

        if (dp[i][j] != -1) return dp[i][j];

        int down = memoize(grid, dp, i + 1, j);
        int right = memoize(grid, dp, i, j + 1);

        return dp[i][j] = (down + right);

        // Complexity analysis 
        // Time : O(2*(N*M)) 
        // Space : O(N+M) stack + O(N*M) memory 
    }

    int tabulation(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size();
        vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));

        if (grid[0][0] == 1 || grid[N - 1][M - 1] == 1) return 0;

        // base 
        dp[N - 1][M - 1] = 1;

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            for (int j = M - 1; j >= 0; j--) {
                if (i == N - 1 && j == M - 1) continue;
                if (grid[i][j] == 1) continue;

                int down = dp[i + 1][j];
                int right = dp[i][j + 1];

                dp[i][j] = ((long long)down + right) % MODO;
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) memory 
    }

    int optimised(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size();

        if (grid[0][0] == 1 || grid[N - 1][M - 1] == 1) return 0;

        vector<int> next(M + 1, 0);

        // base 

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            vector<int> curr(M + 1, 0);
            for (int j = M - 1; j >= 0; j--) {
                if (grid[i][j] == 1) continue;
                if (i == N - 1 && j == M - 1) {
                    curr[j] = 1;
                    continue;
                }

                int down = next[j];
                int right = curr[j + 1];

                curr[j] = ((long long)down + right) % MODO;
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
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // return recursion(obstacleGrid);

        // int N = obstacleGrid.size(), M = obstacleGrid[0].size();
        // vector<vector<int>> dp(N, vector<int>(M, -1));
        // return memoize(obstacleGrid, dp);

        // return tabulation(obstacleGrid);

        return optimised(obstacleGrid);
    }
};

void p1() {
    // Problem 1 : Leetcode 63. Unique Paths II - https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/grid-path-2/0 

    vector<vector<int>> grid = { {0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0} };
    cout << Problem1().uniquePathsWithObstacles(grid) << endl;
}

class Problem2 {
    string solve1(string& s) {
        int len = s.length();
        string out = "";

        for (int i = 0; i < len; i++) {
            for (int j = i; j < len; j++) {
                int low = i, high = j;

                while (low <= high && s[low] == s[high]) low++, high--;

                if (low >= high) {
                    int l2 = (j - i + 1);
                    int l1 = out.length();
                    if (l1 < l2) out = s.substr(i, l2);
                }
            }
        }

        return out;

        // Complexity analysis 
        // Time : O(N*N*N) 
        // Space : O(1) 
    }

    string solve2(string& s) {
        string lpalin = "";

        for (int i = 0, len = s.length(); i < len; i++) {
            // pointers for low and high index 
            int l = 0, h = 0;
            // length of palind sub str 
            int l2 = 0;

            // explore palindromic substr - odd length 
            l = i, h = i;
            while (l >= 0 && h < len && s[l] == s[h]) l--, h++;

            // fix pointers - palindrome substr, remove out of bound indices 
            l = l + 1, h = h - 1;

            l2 = h - l + 1;
            if (l2 > lpalin.length()) {
                lpalin = s.substr(l, l2);
            }

            // explore palindromic substr - even length 
            l = i, h = i + 1;
            while (l >= 0 && h < len && s[l] == s[h]) l--, h++;

            // fix pointers - palindrome substr, remove out of bound indices 
            l = l + 1, h = h - 1;

            l2 = h - l + 1;
            if (l2 > lpalin.length()) {
                lpalin = s.substr(l, l2);
            }
        }

        return lpalin;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

public:
    string longestPalindrome(string s) {
        // return solve1(s);

        return solve2(s);
    }
};

void p2() {
    // Problem 2 : Leetcode 5. Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1 

    cout << Problem2().longestPalindrome("bb") << endl;
    cout << Problem2().longestPalindrome("abb") << endl;
    cout << Problem2().longestPalindrome("abba") << endl;
    cout << Problem2().longestPalindrome("abcba") << endl;
    cout << Problem2().longestPalindrome("ababxa") << endl;
}


int main() {
    // Day 17 of February 

    p1();

    p2();


    return 0;
}