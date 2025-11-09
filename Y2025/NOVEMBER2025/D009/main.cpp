#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int countOperations(int num1, int num2) {
    int operationsCount = 0;

    while (num1 != 0 && num2 != 0) {
      if (num1 >= num2) {
        operationsCount += (num1 / num2);
        num1 %= num2;
      } else {
        operationsCount += (num2 / num1);
        num2 %= num1;
      }
    }

    return operationsCount;

    // Complexity analysis
    // Time : O(log(max(num1, num2)))
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2169. Count Operations to Obtain Zero - https://leetcode.com/problems/count-operations-to-obtain-zero/description/?envType=daily-question&envId=2025-11-09 

  vector<pair<int, int>> testcases = {
    { 2, 3 },
    { 10, 10 },
    { 0, 100000 },
    { 1, 100000 },
    { 1, 0 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->countOperations(tc.first, tc.second) << endl;
  }
}

class Solution2 {
private:
  int N;
  vector<vector<int>> grid;
  vector<vector<vector<int>>> dp;

  int helper(int R1, int C1, int R2) {
    int C2 = R1 + C1 - R2;

    if (R1 >= N || C1 >= N || R2 >= N || C2 >= N || C2 < 0) {
      return INT_MIN;
    }

    if (grid[R1][C1] == -1 || grid[R2][C2] == -1) {
      return INT_MIN;
    }

    if (R1 == N - 1 && C1 == N - 1) {
      return grid[R1][C1];
    }

    if (dp[R1][C1][R2] != -2) {
      return dp[R1][C1][R2];
    }

    int currentChocolates = grid[R1][C1];
    if (R1 != R2 || C1 != C2) {
      currentChocolates += grid[R2][C2];
    }

    int maxFutureChocolates = INT_MIN;

    maxFutureChocolates = max(maxFutureChocolates, helper(R1 + 1, C1, R2 + 1));

    maxFutureChocolates = max(maxFutureChocolates, helper(R1 + 1, C1, R2));

    maxFutureChocolates = max(maxFutureChocolates, helper(R1, C1 + 1, R2 + 1));

    maxFutureChocolates = max(maxFutureChocolates, helper(R1, C1 + 1, R2));

    int totalMax = currentChocolates + maxFutureChocolates;

    if (maxFutureChocolates == INT_MIN) {
      dp[R1][C1][R2] = INT_MIN;
    } else {
      dp[R1][C1][R2] = totalMax;
    }

    return dp[R1][C1][R2];
  }

public:
  int chocolatePickup(vector<vector<int>>& grid) {
    this->grid = grid;
    this->N = grid.size();

    dp.assign(N, vector<vector<int>>(N, vector<int>(N, -2)));

    int result = helper(0, 0, 0);

    return max(0, result);

    // Complexity analysis
    // Time : O(2 * N * N * N)
    // Space : O(N * N * N)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Chocolate Pickup II - https://www.geeksforgeeks.org/problems/chocolate-pickup-ii/1 

  vector<vector<vector<int>>> testcases = {
    { { 0,1,-1 }, { 1,1,-1 }, { 1,1,2 } },
    { { 1,1,0 }, { 1,1,1 }, { 0,1,1 } },
    { { 1,0,-1 }, { 2,-1,-1 }, { 1,-1,3 } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->chocolatePickup(tc) << endl;
  }
}

int main() {
  // Day 9 of November 2025

  p1();

  p2();

  return 0;
}
