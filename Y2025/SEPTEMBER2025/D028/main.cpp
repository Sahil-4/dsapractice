#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int largestPerimeter(vector<int>& nums) {
    // triangle (a,b,c) to be valid if 
    // a + b > c
    // b + c > a
    // c + a > b
    // simplified 
    // x = min(a, b, c)
    // y = max(a, b, c)
    // z = [leftout]
    // x + z > y
    // if we are able to satisfy condition x + z > y
    // we can safely say that triangle is valid 

    sort(nums.begin(), nums.end());
    reverse(nums.begin(), nums.end());

    int N = nums.size();

    for (int i = 0; i < N - 2; i++) {
      int a = nums[i], b = nums[i + 1], c = nums[i + 2];
      if (a < b + c) return a + b + c;
    }

    return 0;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N) + O(N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 976. Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question&envId=2025-09-28 

  vector<vector<int>> testcases = {
    {2,1,2},
    {1,2,1,10},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->largestPerimeter(tc) << endl;
  }
}


class SpecialQueue {
private:
  queue<int> q;
  deque<int> minn;
  deque<int> maxx;

public:
  void enqueue(int x) {
    // Insert element into the queue
    while (!minn.empty() && minn.back() > x) minn.pop_back();
    while (!maxx.empty() && maxx.back() < x) maxx.pop_back();
    q.push(x);
    minn.push_back(x);
    maxx.push_back(x);
  }

  void dequeue() {
    // Remove element from the queue
    if (isEmpty()) return;
    if (q.front() == minn.front()) minn.pop_front();
    if (q.front() == maxx.front()) maxx.pop_front();
    q.pop();
  }

  int getFront() {
    // Get front element
    if (isEmpty()) return 0;
    return q.front();
  }

  int getMin() {
    // Get minimum element
    if (isEmpty()) return 0;
    return minn.front();
  }

  int getMax() {
    // Get maximum element
    if (isEmpty()) return 0;
    return maxx.front();
  }

  bool isEmpty() {
    return q.size() == 0;
  }
};

class Solution2 {
public:
  vector<int> longestSubarray(vector<int>& arr, int x) {
    // code here
    SpecialQueue* sq = new SpecialQueue();

    int N = arr.size();
    vector<int> outputRange = { 0, -1 };

    for (int l = 0, r = 0; r < N; r++) {
      sq->enqueue(arr[r]);

      while (l < r) {
        int minn = sq->getMin();
        int maxx = sq->getMax();
        if (maxx - minn <= x) break;
        sq->dequeue();
        l++;
      }

      if (r - l > outputRange[1] - outputRange[0]) {
        outputRange = { l, r };
      }
    }

    delete sq;

    return vector<int>(arr.begin() + outputRange[0], arr.begin() + outputRange[1] + 1);

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(3N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Longest Bounded-Difference Subarray -https://www.geeksforgeeks.org/problems/longest-bounded-difference-subarray/1 

  vector<pair<vector<int>, int>> testcases = {
    {{8, 4, 5, 6, 7}, 3},
    {{1, 10, 12, 13, 14}, 2},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> out = s2->longestSubarray(tc.first, tc.second);
    for (auto& e : out) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 28 of September 2025

  p1();

  p2();

  return 0;
}
