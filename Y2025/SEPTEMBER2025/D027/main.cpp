#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  double largestTriangleArea(vector<vector<int>>& points) {
    int N = points.size();

    double maxAr = 0.0;

    for (int i = 0; i < N - 2; i++) {
      for (int j = 0; j < N - 1; j++) {
        for (int k = 0; k < N; k++) {
          int xi = points[i][0], yi = points[i][1];
          int xj = points[j][0], yj = points[j][1];
          int xk = points[k][0], yk = points[k][1];

          double a = hypot(xi - xj, yi - yj);
          double b = hypot(xj - xk, yj - yk);
          double c = hypot(xk - xi, yk - yi);

          double s = (a + b + c) * 0.5;
          double ar = sqrt(s * (s - a) * (s - b) * (s - c));

          maxAr = max(maxAr, ar);
        }
      }
    }

    return maxAr;

    // Complexity analysis 
    // Time : O(N^3) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 812. Largest Triangle Area - https://leetcode.com/problems/largest-triangle-area/description/?envType=daily-question&envId=2025-09-27 

  vector<vector<vector<int>>> testcases = {
    { {0,0},{0,1},{1,0},{0,2},{2,0} },
    { { 1,0 },{0,0},{0,1} },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->largestTriangleArea(tc) << endl;
  }
}

class Solution2 {
public:
  int kBitFlips(vector<int>& arr, int k) {
    // code here
    int N = arr.size();

    vector<int> prefix(N + 2, 0);
    int count = 0;

    for (int i = 0; i <= N - k; i++) {
      if (i > 0) {
        prefix[i] += prefix[i - 1];
      }

      if (arr[i] == 0 && !(prefix[i] & 1)) {
        prefix[i] += 1;
        prefix[i + k] -= 1;
        count++;
      }

      if (arr[i] == 1 && (prefix[i] & 1)) {
        prefix[i] += 1;
        prefix[i + k] -= 1;
        count++;
      }
    }

    for (int i = N - k + 1; i < N; i++) {
      prefix[i] += prefix[i - 1];
      if (arr[i] == 0 && prefix[i] % 2 == 0) {
        return -1;
      }

      if (arr[i] == 1 && prefix[i] % 2 == 1) {
        return -1;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimum K Consecutive Bit Flips - https://www.geeksforgeeks.org/problems/minimum-number-of-k-consecutive-bit-flips--171650/1 

  vector<pair<vector<int>, int>> testcases = {
    {{1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1}, 2},
    {{0, 0, 1, 1, 1, 0, 0}, 3}
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->kBitFlips(tc.first, tc.second) << endl;
  }
}

int main() {
  // Day 27 of September 2025

  p1();

  p2();

  return 0;
}
