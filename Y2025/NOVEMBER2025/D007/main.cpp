#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  long long check(vector<int>& stations, int r, int k, long long power) {
    int N = stations.size();

    long long p = 0;
    for (int i = 0; i < r; i++) {
      p += stations[i];
    }

    vector<int> add(N, 0);
    for (int i = 0; i < N; i++) {
      if (i + r < N) {
        p += stations[i + r];
      }

      if (i - r - 1 >= 0) {
        p -= (stations[i - r - 1] + add[i - r - 1]);
      }

      if (p < power) {
        long long extra = power - p;

        if (extra > k) {
          return false;
        }

        k -= extra;
        p += extra;
        add[min(i + r, N - 1)] += extra;
      }
    }

    return true;
  }

public:
  long long maxPower(vector<int>& stations, int r, int k) {
    long long low = 0;
    long long high = 1e18;
    long long ans = 0;

    while (low <= high) {
      long long mid = (low + high) / 2;

      if (check(stations, r, k, mid)) {
        ans = max(ans, mid);
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(N * Log(T))
    // Space : O(N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2528. Maximize the Minimum Powered City - https://leetcode.com/problems/maximize-the-minimum-powered-city/description/?envType=daily-question&envId=2025-11-07 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    {{ 1,2,4,5,0 }, {1, 2}},
    {{ 4,4,4,4 }, {0, 3}},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxPower(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

class Solution2 {
  int getNextJob(vector<vector<int>>& jobs, int s, int low, int high) {
    int ans = high + 1;

    while (low <= high) {
      int mid = low + (high - low) / 2;

      if (jobs[mid][0] >= s) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;
  }

  int recursion(vector<vector<int>>& jobs, int N, int index, vector<int>& memo) {
    if (index >= N) return 0;

    if (memo[index] != -1) return memo[index];

    int nextIndex = getNextJob(jobs, jobs[index][1], index + 1, N - 1);

    int take = jobs[index][2] + recursion(jobs, N, nextIndex, memo);
    int skip = recursion(jobs, N, index + 1, memo);

    return memo[index] = max(take, skip);

    // Complexity analysis
    // Time : O(2 * N * Log(N))
    // Space : O(N) + O(N)
  }

  int tabulation(vector<vector<int>>& jobs, int N) {
    vector<int> memo(N + 1, 0);

    for (int index = N - 1; index >= 0; index--) {
      int nextIndex = getNextJob(jobs, jobs[index][1], index + 1, N - 1);

      int take = jobs[index][2] + memo[nextIndex];
      int skip = memo[index + 1];

      memo[index] = max(take, skip);
    }

    return memo[0];

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(N)
  }

public:
  int maxProfit(vector<vector<int>>& jobs) {
    // code here
    int N = jobs.size();

    auto comp = [&](auto& j1, auto& j2) {
      return j1[0] < j2[0];
      };
    sort(jobs.begin(), jobs.end(), comp);

    // vector<int> memo(N, -1);
    // return recursion(jobs, N, 0, memo);

    return tabulation(jobs, N);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Weighted Job Scheduling - https://www.geeksforgeeks.org/problems/weighted-job-scheduling/1 

  vector<vector<vector<int>>> testcases = {
    {
      { 1, 2, 50 },
      { 3, 5, 20 },
      { 6, 19, 100 },
      { 2, 100, 200 }
    },
    {
      { 1, 3, 60 },
      { 2, 5, 50 },
      { 4, 6, 70 },
      { 5, 7, 30 }
    }
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->maxProfit(tc) << endl;
  }
}

int main() {
  // Day 7 of November 2025

  p1();

  p2();

  return 0;
}
