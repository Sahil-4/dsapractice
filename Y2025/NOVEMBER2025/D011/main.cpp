#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  pair<int, int> count_0s_1s(string str) {
    pair<int, int> p = { 0, 0 };

    for (int i = 0; i < str.size(); i++) {
      p.first += str[i] == '0';
      p.second += str[i] == '1';
    }

    return p;
  }

  int recursion(vector<string>& strs, int z, int o, int index) {
    if (index >= strs.size()) return 0;

    int skip = recursion(strs, z, o, index + 1);

    int take = 0;
    pair<int, int> zeroes_ones = count_0s_1s(strs[index]);
    int zeroes = zeroes_ones.first;
    int ones = zeroes_ones.second;
    if (z >= zeroes && o >= ones) {
      take = 1 + recursion(strs, z - zeroes, o - ones, index + 1);
    }

    return max(skip, take);

    // Complexity analysis
    // Time : O(2^N*str_len)
    // Space : O(N)
  }

  int memoization(vector<string>& strs, int z, int o, int index, vector<vector<vector<int>>>& memo) {
    if (index >= strs.size()) return 0;

    if (memo[index][z][o] != -1) return memo[index][z][o];

    int skip = memoization(strs, z, o, index + 1, memo);

    int take = 0;
    pair<int, int> zeroes_ones = count_0s_1s(strs[index]);
    int zeroes = zeroes_ones.first;
    int ones = zeroes_ones.second;
    if (z >= zeroes && o >= ones) {
      take = 1 + memoization(strs, z - zeroes, o - ones, index + 1, memo);
    }

    return memo[index][z][o] = max(skip, take);

    // Complexity analysis
    // Time : O(2*N*m*n*str_len)
    // Space : O(N*m*n) + O(N)
  }

  int tabulation(vector<string>& strs, int N, int m, int n) {
    vector<vector<int>> next(m + 1, vector<int>(n + 1, 0));

    for (int index = N - 1; index >= 0; index--) {
      vector<vector<int>> curr(m + 1, vector<int>(n + 1, 0));

      for (int z = 0; z <= m; z++) {
        for (int o = 0; o <= n; o++) {
          int skip = next[z][o];

          int take = 0;
          pair<int, int> zeroes_ones = count_0s_1s(strs[index]);
          int zeroes = zeroes_ones.first;
          int ones = zeroes_ones.second;
          if (z >= zeroes && o >= ones) {
            take = 1 + next[z - zeroes][o - ones];
          }

          curr[z][o] = max(skip, take);
        }
      }

      next = curr;
    }

    return next[m][n];

    // Complexity analysis
    // Time : O(N*m*n*str_len)
    // Space : O(m*n)
  }

  int optimised(vector<string>& strs, int N, int m, int n) {
    vector<vector<int>> next(m + 1, vector<int>(n + 1, 0));
    vector<pair<int, int>> strsOnesZeroes;
    for (auto& str : strs) {
      strsOnesZeroes.push_back(count_0s_1s(str));
    }

    for (int index = N - 1; index >= 0; index--) {
      vector<vector<int>> curr(m + 1, vector<int>(n + 1, 0));

      for (int z = 0; z <= m; z++) {
        for (int o = 0; o <= n; o++) {
          int skip = next[z][o];

          int take = 0;
          pair<int, int> zeroes_ones = strsOnesZeroes[index];
          int zeroes = zeroes_ones.first;
          int ones = zeroes_ones.second;
          if (z >= zeroes && o >= ones) {
            take = 1 + next[z - zeroes][o - ones];
          }

          curr[z][o] = max(skip, take);
        }
      }

      next = curr;
    }

    return next[m][n];

    // Complexity analysis
    // Time : O(N*str_len) + O(N*m*n)
    // Space : O(N) + O(m*n)
  }

public:
  int findMaxForm(vector<string>& strs, int m, int n) {
    // return recursion(strs, m, n, 0);

    int N = strs.size();
    // vector<vector<vector<int>>> memo(N, vector<vector<int>>(m+1, vector<int>(n+1, -1)));
    // return memoization(strs, m, n, 0, memo);

    // return tabulation(strs, N, m, n);

    return optimised(strs, N, m, n);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 474. Ones and Zeroes - https://leetcode.com/problems/ones-and-zeroes/description/?envType=daily-question&envId=2025-11-11 

  vector<pair<vector<string>, pair<int, int>>> testcases = {
    { { "10","0001","111001","1","0" }, { 5,3 } },
    { { "10","0","1" }, { 1,1 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->findMaxForm(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

class Solution2 {
  int recursion(string& s1, int s1i, string& s2, int s2i) {
    if (s1i >= s1.size()) return s2.size() - s2i;
    if (s2i >= s2.size()) return s1.size() - s1i;

    if (s1[s1i] == s2[s2i]) {
      return 1 + recursion(s1, s1i + 1, s2, s2i + 1);
    } else {
      int c1 = recursion(s1, s1i + 1, s2, s2i);
      int c2 = recursion(s1, s1i, s2, s2i + 1);
      return 1 + min(c1, c2);
    }

    // Complexity analysis
    // Time : O(2^N+M)
    // Space : O(N+M)
  }

  int memoization(string& s1, int s1i, string& s2, int s2i, vector<vector<int>>& memo) {
    if (s1i >= s1.size()) return s2.size() - s2i;
    if (s2i >= s2.size()) return s1.size() - s1i;

    if (memo[s1i][s2i] != -1) return memo[s1i][s2i];

    if (s1[s1i] == s2[s2i]) {
      return memo[s1i][s2i] = 1 + memoization(s1, s1i + 1, s2, s2i + 1, memo);
    } else {
      int c1 = memoization(s1, s1i + 1, s2, s2i, memo);
      int c2 = memoization(s1, s1i, s2, s2i + 1, memo);
      return memo[s1i][s2i] = 1 + min(c1, c2);
    }

    // Complexity analysis
    // Time : O(2*N*M)
    // Space : O(N*M) + O(N+M)
  }

  int tabulation(string& s1, int s1len, string& s2, int s2len) {
    vector<vector<int>> memo(s1len + 1, vector<int>(s2len + 1, 0));

    for (int i = 0; i <= s1len; i++) {
      memo[i][s2len] = s1len - i;
    }

    for (int j = 0; j <= s2len; j++) {
      memo[s1len][j] = s2len - j;
    }

    for (int s1i = s1len - 1; s1i >= 0; s1i--) {
      for (int s2i = s2len - 1; s2i >= 0; s2i--) {
        if (s1[s1i] == s2[s2i]) {
          memo[s1i][s2i] = 1 + memo[s1i + 1][s2i + 1];
        } else {
          int c1 = memo[s1i + 1][s2i];
          int c2 = memo[s1i][s2i + 1];
          memo[s1i][s2i] = 1 + min(c1, c2);
        }
      }
    }

    return memo[0][0];

    // Complexity analysis
    // Time : O(N*M)
    // Space : O(N*M)
  }

public:
  int minSuperSeq(string& s1, string& s2) {
    // code here
    // s1 = "AGGTAB", s2 = "GXTXAYB"
    // s = "AGGXTXAYB"

    // return recursion(s1, 0, s2, 0);

    int s1len = s1.size();
    int s2len = s2.size();
    // vector<vector<int>> memo(s1len, vector<int>(s2len, -1));
    // return memoization(s1, 0, s2, 0, memo);

    return tabulation(s1, s1len, s2, s2len);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Shortest Common Supersequence - https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1 

  vector<pair<string, string>> testcases = {
    { "geek", "eke" },
    { "AGGTAB", "GXTXAYB" },
    { "geek", "ek" },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->minSuperSeq(tc.first, tc.second) << endl;
  }
}

int main() {
  // Day 11 of November 2025

  p1();

  p2();

  return 0;
}
