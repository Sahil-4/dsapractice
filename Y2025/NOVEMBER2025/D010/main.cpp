#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int minOperations(vector<int>& nums) {
    int N = nums.size();

    vector<int> nextSmaller(N, N);
    unordered_map<int, set<int>> mp;
    for (int i = 0; i < N; i++) {
      mp[nums[i]].insert(i);
    }

    stack<int> stk;
    stk.push(N - 1);
    for (int i = N - 2; i >= 0; i--) {
      while (!stk.empty() && nums[i] <= nums[stk.top()]) {
        stk.pop();
      }

      if (!stk.empty()) {
        nextSmaller[i] = stk.top();
      }

      stk.push(i);
    }

    int operations = 0;

    for (int i = 0; i < N; i++) {
      if (nums[i] == 0) continue;

      int j = nextSmaller[i];
      operations++;

      for (int ni : mp[nums[i]]) {
        if (ni >= j) break;

        mp[nums[i]].erase(ni);
        nums[ni] = 0;
      }
    }

    return operations;

    // Complexity analysis
    // Time : O(4N)
    // Space : O(2N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3542. Minimum Operations to Convert All Elements to Zero - https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/?envType=daily-question&envId=2025-11-10 

  vector<vector<int>> testcases = {
    { 0, 2 },
    { 3, 1, 2, 1 },
    { 1, 2, 1, 2, 1, 2 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minOperations(tc) << endl;
  }
}

class Solution2 {
  int recursion(vector<int>& arr, int index, bool holding) {
    if (index >= arr.size()) return 0;

    int c1 = 0, c2 = 0;

    if (holding) {
      // keep holding 
      c1 = recursion(arr, index + 1, holding);

      // sell 
      c2 = arr[index] + recursion(arr, index + 2, !holding);
    } else {
      // dont buy 
      c1 = recursion(arr, index + 1, holding);

      // buy 
      c2 = -arr[index] + recursion(arr, index + 1, !holding);
    }

    return max(c1, c2);

    // Complexity analysis
    // Time : O(2 ^ N)
    // Space : O(N)
  }

  int memoization(vector<int>& arr, int index, bool holding, vector<vector<int>>& memo) {
    if (index >= arr.size()) return 0;

    if (memo[index][holding] != -1) {
      return memo[index][holding];
    }

    int c1 = 0, c2 = 0;

    if (holding) {
      // keep holding 
      c1 = memoization(arr, index + 1, holding, memo);

      // sell 
      c2 = arr[index] + memoization(arr, index + 2, !holding, memo);
    } else {
      // dont buy 
      c1 = memoization(arr, index + 1, holding, memo);

      // buy 
      c2 = -arr[index] + memoization(arr, index + 1, !holding, memo);
    }

    return memo[index][holding] = max(c1, c2);

    // Complexity analysis
    // Time : O(2 * N * 2)
    // Space : O(N * 2) + O(N)
  }

  int tabulation(vector<int>& arr, int N) {
    vector<vector<int>> memo(N + 2, vector<int>(2, 0));

    for (int index = N - 1; index >= 0; index--) {
      for (int holding = 1; holding >= 0; holding--) {
        int c1 = 0, c2 = 0;

        if (holding) {
          // keep holding 
          c1 = memo[index + 1][holding];

          // sell 
          c2 = arr[index] + memo[index + 2][!holding];
        } else {
          // dont buy 
          c1 = memo[index + 1][holding];

          // buy 
          c2 = -arr[index] + memo[index + 1][!holding];
        }

        memo[index][holding] = max(c1, c2);
      }
    }

    return memo[0][0];

    // Complexity analysis
    // Time : O(N * 2)
    // Space : O(N * 2)
  }

  int optimised(vector<int>& arr, int N) {
    // vector<vector<int>> memo(N + 2, vector<int>(2, 0));
    vector<int> plus2(2, 0);
    vector<int> plus1(2, 0);

    for (int index = N - 1; index >= 0; index--) {
      vector<int> plus0(2, 0);
      for (int holding = 1; holding >= 0; holding--) {
        int c1 = 0, c2 = 0;

        if (holding) {
          // keep holding 
          c1 = plus1[holding];

          // sell 
          c2 = arr[index] + plus2[!holding];
        } else {
          // dont buy 
          c1 = plus1[holding];

          // buy 
          c2 = -arr[index] + plus1[!holding];
        }

        plus0[holding] = max(c1, c2);
      }

      plus2 = plus1;
      plus1 = plus0;
    }

    return plus1[0];

    // Complexity analysis
    // Time : O(N * 2)
    // Space : O(3 * 2)
  }

public:
  int maxProfit(vector<int>& arr) {
    // code here
    int N = arr.size();

    // return recursion(arr, 0, false);

    // vector<vector<int>> memo(N, vector<int>(2, -1));
    // return memoization(arr, 0, false, memo);

    // return tabulation(arr, N);

    return optimised(arr, N);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Stock Buy and Sell with Cooldown - https://www.geeksforgeeks.org/problems/buy-stock-with-cooldown/1 

  vector<vector<int>> testcases = {
    {0, 2, 1, 2, 3},
    {3, 1, 6, 1, 2, 4},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->maxProfit(tc) << endl;
  }
}

int main() {
  // Day 10 of November 2025

  p1();

  p2();

  return 0;
}
