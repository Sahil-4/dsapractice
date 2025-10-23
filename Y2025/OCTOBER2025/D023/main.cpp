#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  bool hasSameDigits(string s) {
    int N = s.size();

    while (N > 2) {
      for (int i = 1; i < s.size(); i++) {
        char ch = '0' + (((s[i] - '0') + (s[i - 1] - '0')) % 10);
        s[i - 1] = (ch);
      }

      N--;
    }

    return s[0] == s[1];

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3461. Check If Digits Are Equal in String After Operations I - https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-23 

  vector<string> testcases = {
    "3902", "34789"
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << (s1->hasSameDigits(tc) ? "true" : "false") << endl;
  }
}

class Solution2 {
  int getEuclideanDistanceFromOrigin(vector<int>& point) {
    // sqrt( (x2 - x1)2 + (y2 - y1)2 )
    int x2 = point[0], y2 = point[1];
    return (x2 * x2) + (y2 * y2);
  }

public:
  vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // code here

    priority_queue<pair<int, vector<int>>> heap;

    for (auto& point : points) {
      int euD = getEuclideanDistanceFromOrigin(point);
      heap.push({ euD, { point[0], point[1] } });

      if (heap.size() > k) heap.pop();
    }

    vector<vector<int>> close;
    while (!heap.empty()) {
      close.push_back(heap.top().second);
      heap.pop();
    }

    return close;

    // Complexity analysis 
    // Time : O(N*Log(K)) + O(K) 
    // Space : O(K) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks K Closest Points to Origin - https://www.geeksforgeeks.org/problems/k-closest-points-to-origin--172242/1 

  vector<pair<vector<vector<int>>, int>> testcases = {
    { {{1, 3}, {-2, 2}, {5, 8}, {0, 1}}, 2 },
    { {{1, 3}, {-2, 2}, {5, 8}, {0, 1}}, 3 },
    { {{2, 4}, {-1, -1}, {0, 0}}, 1 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<vector<int>> kClosest = s2->kClosest(tc.first, tc.second);
    for (auto& point : kClosest) {
      cout << "[ " << point[0] << ", " << point[1] << " ]" << endl;
    } cout << endl;
  }
}

int main() {
  // Day 23 of October 2025

  p1();

  p2();

  return 0;
}
