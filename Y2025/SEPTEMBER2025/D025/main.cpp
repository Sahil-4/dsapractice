#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int INITIAL = -1000000;

  int memoize(vector<vector<int>>& triangle, int N, int r, int c, vector<vector<int>>& memo) {
    if (r >= N) return 0;

    if (memo[r][c] != INITIAL) return memo[r][c];

    int op1 = memoize(triangle, N, r + 1, c + 0, memo);
    int op2 = memoize(triangle, N, r + 1, c + 1, memo);
    memo[r][c] = triangle[r][c] + min(op1, op2);

    return memo[r][c];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(N) stack + O(N * N) memory space 
  }

  int tabulation(vector<vector<int>>& triangle, int N) {
    vector<vector<int>> memo(N + 1, vector<int>(N + 1, 0));

    for (int r = N - 1; r >= 0; r--) {
      for (int c = r; c >= 0; c--) {
        int op1 = memo[r + 1][c + 0];
        int op2 = memo[r + 1][c + 1];
        memo[r][c] = triangle[r][c] + min(op1, op2);
      }
    }

    return memo[0][0];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(N * N) memory space 
  }

  int optimised(vector<vector<int>>& triangle, int N) {
    vector<int> next(N + 1, 0);

    for (int r = N - 1; r >= 0; r--) {
      vector<int> curr(N + 1, 0);
      for (int c = r; c >= 0; c--) {
        int op1 = next[c + 0];
        int op2 = next[c + 1];
        curr[c] = triangle[r][c] + min(op1, op2);
      }
      next = curr;
    }

    return next[0];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(2 * N) memory space 
  }

public:
  int minimumTotal(vector<vector<int>>& triangle) {
    int N = triangle.size();
    // return recursion(triangle, N, 0, 0);

    // vector<vector<int>> memo(N, vector<int>(N, INITIAL));
    // return memoize(triangle, N, 0, 0, memo);

    // return tabulation(triangle, N);
    return optimised(triangle, N);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 120. Triangle - https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25 

  Solution1* s1 = new Solution1();

  vector<vector<int>> tc1 = { {2},{3,4},{6,5,7},{4,1,8,3} };
  vector<vector<int>> tc2 = { {-10} };
  cout << s1->minimumTotal(tc1) << endl;
  cout << s1->minimumTotal(tc2) << endl;
}

class Solution2 {
private:
  string getNormalise(const string& bits) {
    int start = 0;
    while (start < 32) {
      if (bits[start] == '1') break;
      start++;
    }

    return bits.substr(start);
  }

  void updateNextBit(string& bits) {
    for (int bi = 31; bi >= 0; bi--) {
      if (bits[bi] == '0') {
        bits[bi] = '1';
        break;
      }

      bits[bi] = '0';
    }
  }

public:
  vector<string> generateBinary(int n) {
    // code here
    // n = 4
    // bits = "...0000"
    // i = 1
    // bits = "...0001"
    // nums = ["1"] 
    // i = 2
    // bits = "...0010"
    // nums = ["1", 10"] 
    // i = 3
    // bits = "...0011"
    // nums = ["1", "10", "11"] 
    // i = 4
    // bits = "...0100"
    // nums = ["1", "10", "11", "100"] 

    vector<string> binaryNums;
    string bits(32, '0');

    for (int i = 1; i <= n; i++) {
      updateNextBit(bits);
      string binary_i = getNormalise(bits);
      binaryNums.push_back(binary_i);
    }

    return binaryNums;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Generate Binary Numbers - https://www.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1 

  Solution2* s2 = new Solution2();
  // vector<string> binaries = s2->generateBinary(10);
  vector<string> binaries = s2->generateBinary(100);
  // vector<string> binaries = s2->generateBinary(1000000);
  for (auto& bin : binaries) cout << bin << endl;
}

int main() {
  // Day 25 of September 2025

  p1();

  p2();

  return 0;
}
