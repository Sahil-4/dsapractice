#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int recursion(vector<int>& values, int l, int r) {
    if (l + 1 == r) return 0;

    int opAnswer = INT_MAX;

    for (int k = l + 1; k < r; k++) {
      int curr = values[l] * values[r] * values[k];
      int sub1 = recursion(values, l, k);
      int sub2 = recursion(values, k, r);
      int sum = curr + sub1 + sub2;
      opAnswer = min(opAnswer, sum);
    }

    return opAnswer;

    // Complexity analysis 
    // Time : O(N^N) 
    // Space : O(N) 
  }

  int memoized(vector<int>& values, int l, int r, vector<vector<int>>& memo) {
    if (l + 1 == r) return 0;

    if (memo[l][r] != -1) return memo[l][r];

    int opAnswer = INT_MAX;

    for (int k = l + 1; k < r; k++) {
      int curr = values[l] * values[r] * values[k];
      int sub1 = memoized(values, l, k, memo);
      int sub2 = memoized(values, k, r, memo);
      int sum = curr + sub1 + sub2;
      opAnswer = min(opAnswer, sum);
    }

    return memo[l][r] = opAnswer;

    // Complexity analysis 
    // Time : O(N*N*2) 
    // Space : O(N*N) + O(N) 
  }

  int tabulation(vector<int>& values, int N) {
    vector<vector<int>> memo(N + 1, vector<int>(N + 1, 0));

    for (int l = N - 1; l >= 0; l--) {
      for (int r = l + 2; r < N; r++) {
        int opAnswer = INT_MAX;

        for (int k = l + 1; k < r; k++) {
          int curr = values[l] * values[r] * values[k];
          int sub1 = memo[l][k];
          int sub2 = memo[k][r];
          int sum = curr + sub1 + sub2;
          opAnswer = min(opAnswer, sum);
        }

        memo[l][r] = opAnswer;
      }
    }

    return memo[0][N - 1];

    // Complexity analysis 
    // Time : O(N*N*2) 
    // Space : O(N*N) 
  }

public:
  int minScoreTriangulation(vector<int>& values) {
    int N = values.size();
    // return recursion(values, 0, N - 1);

    // vector<vector<int>> memo(N, vector<int>(N, -1));
    // return memoized(values, 0, N - 1, memo);

    return tabulation(values, N);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1039. Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/?envType=daily-question&envId=2025-09-29 

  vector<vector<int>> testcases = {
    {1,2,3},
    {3,7,4,5},
    {1,3,1,4,1,5},
    {100,50,100,50,100,100,50,100,50,100,100,50,100,50,100},
    {100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100},
    {100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100,100,50,100,50,100},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minScoreTriangulation(tc) << endl;
  }
}

class Solution2 {
  int bruteForce(vector<int>& arr, int a, int b) {
    int N = arr.size();
    int answer = 0;

    for (int si = 0; si < N - a; si++) {
      int sum = 0;
      for (int j = si; j < N; j++) {
        sum += arr[j];
        int len = j - si + 1;
        if (len >= a && len <= b) {
          answer = max(answer, sum);
        }
      }
    }

    return answer;

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(1) 
  }

  int optimal(vector<int>& arr, int a, int b) {
    int N = arr.size();

    // compute prefix sum 
    vector<int> prefix(N + 1, 0);
    for (int i = 1; i <= N; i++) {
      prefix[i] = prefix[i - 1] + arr[i - 1];
    }

    long long answer = INT_MIN;

    // stores index of prefix sum in increasing order 
    // front = min prefix sum index 
    deque<int> dq;

    for (int r = 0; r < N; r++) {
      int end = r + 1 - a;
      // monotonic nature 
      if (end >= 0) {
        while (!dq.empty() && prefix[dq.back()] >= prefix[end]) {
          dq.pop_back();
        }
        dq.push_back(end);
      }

      int start = r + 1 - b;
      // rmeove out of window 
      while (!dq.empty() && dq.front() < start) {
        dq.pop_front();
      }

      // update answer 
      if (!dq.empty()) {
        int l = dq.front();
        long long tanswer = prefix[r + 1] - prefix[l];
        answer = max(answer, tanswer);
      }
    }

    return (int)answer;

    // Complexity analysis 
    // Time : O(N + N) 
    // Space : O(N + N) 
  }

public:
  int maxSubarrSum(vector<int>& arr, int a, int b) {
    // code here

    // return bruteForce(arr, a, b);
    return optimal(arr, a, b);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Maximum subarray sum 2 - https://www.geeksforgeeks.org/problems/maximum-subarray-sum--110820/1 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    {{-1, 3, -1, -2, 5, 3, -5, 2, 2},{3,5}},
    {{3, -1, -2, 5, 3, -5, 2, 2},{3,5}},
    {{4, 5, -1, -2, 6},{2,4}},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->maxSubarrSum(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

int main() {
  // Day 29 of September 2025

  p1();

  p2();

  return 0;
}
