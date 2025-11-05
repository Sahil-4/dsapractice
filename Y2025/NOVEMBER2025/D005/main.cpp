#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  long long sum = 0; //maintains sum of top x elements from main set
  set<pair<int, int>> main; //contains top-x freq, elements
  set<pair<int, int>> sec; //contains remaining freq, leements

  void insertInSet(const pair<int, int>& p, int x) {
    if (main.size() < x || p > *main.begin()) {
      sum += 1LL * p.first * p.second;
      main.insert(p);

      if (main.size() > x) {
        auto smallest = *main.begin();
        sum -= 1LL * smallest.first * smallest.second;
        main.erase(smallest);
        sec.insert(smallest);
      }
    } else {
      sec.insert(p);
    }
  }

  void removeFromSet(const pair<int, int>& p, int x) {
    if (main.find(p) != main.end()) {
      sum -= 1LL * p.first * p.second;
      main.erase(p);

      if (!sec.empty()) {
        auto largest = *sec.rbegin();
        sec.erase(largest);
        main.insert(largest);
        sum += 1LL * largest.first * largest.second;
      }
    } else {
      sec.erase(p);
    }
  }

  vector<long long> findXSum(vector<int>& nums, int k, int x) {
    int n = nums.size();
    sum = 0;

    vector<long long> result;

    unordered_map<int, int> mp; //element -> freq

    int i = 0;
    int j = 0;
    while (j < n) {
      if (mp[nums[j]] > 0) {
        removeFromSet({ mp[nums[j]], nums[j] }, x);
      }

      mp[nums[j]]++; //new freq
      insertInSet({ mp[nums[j]], nums[j] }, x);

      if (j - i + 1 == k) {
        result.push_back(sum);

        removeFromSet({ mp[nums[i]], nums[i] }, x);
        mp[nums[i]]--;
        if (mp[nums[i]] == 0) {
          mp.erase(nums[i]);
        } else {
          insertInSet({ mp[nums[i]], nums[i] }, x);
        }
        i++;
      }

      j++;
    }

    return result;

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(2N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3321. Find X-Sum of All K-Long Subarrays II - https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/description/?envType=daily-question&envId=2025-11-05 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 1,1,2,2,3,4,2,3 }, { 6, 2 } },
    { { 3,8,7,8,7,5 }, { 2, 2 } },
  };

  for (auto& tc : testcases) {
    Solution1* s1 = new Solution1();
    vector<long long> kxSum = s1->findXSum(tc.first, tc.second.first, tc.second.second);
    for (auto sum : kxSum) cout << sum << " ";
    cout << endl;
  }
}

class Solution2 {
  int recursion(int n, int i, vector<vector<int>>& memo) {
    if (n == 0) return 0;

    if (memo[n][i] != -1) return memo[n][i];

    int cprod = i * i;

    if (cprod > n) return 10000;

    int c1 = 1 + recursion(n - cprod, i, memo);
    int c2 = 0 + recursion(n, i + 1, memo);

    return memo[n][i] = min(c1, c2);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N)
  }

  int tabulation(int nn) {
    vector<vector<int>> memo(nn + 1, vector<int>(nn + 1, 1000));

    for (int i = nn; i >= 1; i--) memo[i][0] = 0;

    for (int n = 1; n <= nn; n++) {
      for (int i = nn; i >= 1; i--) {
        int cprod = i * i;

        if (cprod > n) {
          memo[i][n] = 10000;
        } else {
          int c1 = 1 + memo[i][n - cprod];
          int c2 = 0 + memo[i + 1][n];

          memo[i][n] = min(c1, c2);
        }
      }
    }

    return memo[1][nn];

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(N * N)
  }

  int optimised(int nn) {
    // vector<vector<int>> memo(nn+1, vector<int>(nn+1, 1000));
    vector<int> next(nn + 1, 1000);
    next[0] = 0;

    // for (int i = nn; i >= 1; i--) memo[i][0] = 0;

    for (int i = nn; i >= 1; i--) {
      vector<int> curr(nn + 1, 1000);
      curr[0] = 0;

      for (int n = 1; n <= nn; n++) {
        int cprod = i * i;

        if (cprod > n) {
          curr[n] = 10000;
        } else {
          int c1 = 1 + curr[n - cprod];
          int c2 = 0 + next[n];

          curr[n] = min(c1, c2);
        }
      }

      next = curr;
    }

    return next[nn];

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(2N)
  }

public:
  int minSquares(int n) {
    // Code here

    // vector<vector<int>> memo(n+1, vector<int>(n+1, -1));
    // return recursion(n, 1, memo);
    // return tabulation(n);
    return optimised(n);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Get Minimum Squares - https://www.geeksforgeeks.org/problems/get-minimum-squares0538/1 

  vector<int> testcases = {
    1, 6, 10, 100, 208, 1000, 777,
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->minSquares(tc) << endl;
  }
}

int main() {
  // Day 5 of November 2025

  p1();

  p2();

  return 0;
}
