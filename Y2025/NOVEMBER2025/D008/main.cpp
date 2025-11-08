#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int minimumOneBitOperations(int n) {
    if (n == 0) return 0;

    vector<long long> func(32, 0);
    func[0] = 1;
    for (int bi = 1; bi <= 31; bi++) {
      func[bi] = 2 * func[bi - 1] + 1;
    }

    int operations = 0;
    int sign = 1;

    for (int bi = 30; bi >= 0; bi--) {
      int ithBit = ((1 << bi) & n);

      if (ithBit == 0) continue;

      operations += func[bi] * sign;
      sign *= -1;
    }

    return operations;

    // Complexity analysis
    // Time : O(32)
    // Space : O(32)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1611. Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2025-11-08 

  vector<int> testcases = { 3, 6 };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minimumOneBitOperations(tc) << endl;
  }
}

class Solution2 {
  int n = 0;
  int m = 0;

  int recursion(vector<vector<int>>& mat, int k, int r, int c, vector<vector<vector<int>>>& memo) {
    if (r >= n || c >= m) return 0;
    if (r == n - 1 && c == m - 1) return k == mat[r][c];

    if (memo[r][c][k] != -1) return memo[r][c][k];

    int right = recursion(mat, k - mat[r][c], r, c + 1, memo);
    int bottom = recursion(mat, k - mat[r][c], r + 1, c, memo);

    return memo[r][c][k] = (right + bottom);

    // Complexity analysis
    // Time : O(2 * N * M * K)
    // Space : O(N * M * K) + O(N + M)
  }

  int tabulation(vector<vector<int>>& mat, int k) {
    vector<vector<vector<int>>> memo(n, vector<vector<int>>(m, vector<int>(k + 1, 0)));

    if (mat[n - 1][m - 1] <= k) {
      memo[n - 1][m - 1][mat[n - 1][m - 1]] = 1;
    }

    for (int r = n - 1; r >= 0; r--) {
      for (int c = m - 1; c >= 0; c--) {
        if (r == n - 1 && c == m - 1) continue;

        int val = mat[r][c];

        for (int rem = 0; rem <= k; rem++) {
          if (rem - val < 0) continue;

          int right = 0;
          if (c + 1 < m) {
            right = memo[r][c + 1][rem - val];
          }

          int bottom = 0;
          if (r + 1 < n) {
            bottom = memo[r + 1][c][rem - val];
          }

          memo[r][c][rem] = (right + bottom);
        }
      }
    }

    return memo[0][0][k];

    // Complexity analysis
    // Time : O(N * M * K)
    // Space : O(N * M * K)
  }

public:
  int numberOfPath(vector<vector<int>>& mat, int k) {
    // Code Here
    n = mat.size();
    m = mat[0].size();

    // vector<vector<vector<int>>> memo(n, vector<vector<int>>(m, vector<int>(k+1, -1)));
    // return recursion(mat, k, 0, 0, memo);

    return tabulation(mat, k);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Number of paths in a matrix with k coins - https://www.geeksforgeeks.org/problems/number-of-paths-in-a-matrix-with-k-coins2728/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    {12, { { 1, 2, 3 }, { 4, 6, 5 },{ 3, 2, 1 } } },
    {16, { { 1, 2, 3 }, { 4, 6, 5 }, { 9, 8, 7 } } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->numberOfPath(tc.second, tc.first) << endl;
  }
}

int main() {
  // Day 8 of November 2025

  p1();

  p2();

  return 0;
}
