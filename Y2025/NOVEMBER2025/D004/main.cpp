#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int sumOfTopX(unordered_map<int, int>& mp, int x) {
    vector<vector<int>> ans;
    for (auto i : mp) {
      ans.push_back({ i.second, i.first });
    }

    sort(ans.begin(), ans.end());
    reverse(ans.begin(), ans.end());

    int xSum = 0;
    int m = ans.size();
    for (int i = 0; i < min(x, m); i++) {
      xSum += (ans[i][1] * ans[i][0]);
    }

    return xSum;
  }

public:
  vector<int> findXSum(vector<int>& nums, int k, int x) {
    unordered_map<int, int> mp;
    vector<int> ans;

    int n = nums.size();
    for (int i = 0; i < k; i++) {
      mp[nums[i]]++;
    }

    ans.push_back(sumOfTopX(mp, x));

    for (int i = k; i < n; i++) {
      mp[nums[i - k]]--;
      mp[nums[i]]++;

      if (mp[nums[i - k]] == 0) {
        mp.erase(nums[i - k]);
      }

      ans.push_back(sumOfTopX(mp, x));
    }

    return ans;

    // Complexity analysis
    // Time : O(N * K * Log(K))
    // Space : O(N + K)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3318. Find X-Sum of All K-Long Subarrays I - https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/?envType=daily-question&envId=2025-11-04 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 1,1,2,2,3,4,2,3 }, { 6, 2 } },
    { { 3,8,7,8,7,5 }, { 2, 2 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<int> kxSum = s1->findXSum(tc.first, tc.second.first, tc.second.second);
    for (int sum : kxSum) cout << sum << " ";
    cout << endl;
  }
}

class Solution2 {
  int recursion(vector<int>& height, int n, int index, vector<int>& memo) {
    if (index >= n) return 100000;
    if (index == n - 1) return 0;

    if (memo[index] != -1) {
      return memo[index];
    }

    // i -> i + 1
    int op1 = abs(height[index] - height[index + 1]) + recursion(height, n, index + 1, memo);

    // i -> i + 2
    int op2 = abs(height[index] - height[index + 2]) + recursion(height, n, index + 2, memo);

    return memo[index] = min(op1, op2);
  }

  int tabulation(vector<int>& height, int n) {
    int plus2 = 100000;
    int plus1 = 0;
    int plus0 = 0;

    for (int index = n - 2; index >= 0; index--) {
      // i -> i + 1
      int op1 = abs(height[index] - height[index + 1]) + plus1;

      // i -> i + 2
      int op2 = abs(height[index] - height[index + 2]) + plus2;

      plus0 = min(op1, op2);
      plus2 = plus1;
      plus1 = plus0;
    }

    return plus0;
  }

public:
  int minCost(vector<int>& height) {
    // Code here

    int n = height.size();

    // vector<int> memo(n, -1);
    // return recursion(height, n, 0, memo);

    return tabulation(height, n);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Frog Jump - https://www.geeksforgeeks.org/problems/geek-jump/1 

  vector<vector<int>> testcases = {
    { 20, 30, 40, 20 },
    { 30, 20, 50, 10, 40 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->minCost(tc) << endl;
  }
}

int main() {
  // Day 4 of November 2025

  p1();

  p2();

  return 0;
}
