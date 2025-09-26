#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int triangleNumber(vector<int>& nums) {
    // for a valid triangle (a, b, c)
    // if a < b < c
    // a + b > c holds true 

    int N = nums.size();
    int count = 0;

    if (N < 3) return 0;

    vector<int> copy(nums);
    sort(copy.begin(), copy.end());

    for (int s1i = 0; s1i < N; s1i++) {
      for (int s2i = s1i + 1; s2i < N; s2i++) {
        int side1 = copy[s1i], side2 = copy[s2i];
        // for (int s3i = s2i + 1; s3i < N; s3i++) {
        //     int side3 = copy[s3i];
        //     if (side1 + side2 > side3) count++;
        // }
        int needed = side1 + side2;
        auto it = lower_bound(copy.begin(), copy.end(), needed);
        count += max((int)distance(copy.begin() + s2i, it) - 1, 0);
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) + O(N * N * Log(N)) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 611. Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/description/?envType=daily-question&envId=2025-09-26 

  vector<vector<int>> testcases = {
    { 2,2,3,4},
    { 4,2,3,4 },
    { 1,2,3,4,5,6,7,8,9,10 },
    { 1,8,9,10,2,5,6,7,3,4 },
    { 1,8,9,10,7,8,9,10,2,5,6,7,3,4,9,10,7,8,9,10,2,5,6,7,3,4 },
    { 10,30,90,100 },
    { 0,0 },
    { 0,0,0 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->triangleNumber(tc) << endl;
  }
}

class Solution2 {
private:
  void rotateDequeLeft(deque<int>& dq, int k) {
    while (k > 0) {
      int el = dq.front();
      dq.pop_front();
      dq.push_back(el);
      k--;
    }
  }

  void rotateDequeRight(deque<int>& dq, int k) {
    while (k > 0) {
      int el = dq.back();
      dq.pop_back();
      dq.push_front(el);
      k--;
    }
  }

public:
  void rotateDeque(deque<int>& dq, int type, int k) {
    // code here
    k = k % dq.size();
    type == 1 ? rotateDequeRight(dq, k) : rotateDequeLeft(dq, k);

    // Complexity analysis 
    // Time : O(K) 
    // Space : O(1) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Rotate Deque By K - https://www.geeksforgeeks.org/problems/rotate-deque-by-k/1 

  deque<int> tc = { 1, 2, 3, 4, 5, 6 };

  Solution2* s2 = new Solution2();
  // s2->rotateDeque(tc, 1, 2);
  // s2->rotateDeque(tc, 2, 2);
  s2->rotateDeque(tc, 1, 14);
  // s2->rotateDeque(tc, 2, 14);

  while (!tc.empty()) {
    cout << tc.front() << " ";
    tc.pop_front();
  } cout << endl;
}

int main() {
  // Day 26 of September 2025

  p1();

  p2();

  return 0;
}
