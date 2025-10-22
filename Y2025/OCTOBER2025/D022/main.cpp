#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxFrequency(vector<int>& nums, int k, int numOperations) {
    int N = nums.size();

    int maxi = *max_element(nums.begin(), nums.end()) + k;

    map<int, int> difference;
    unordered_map<int, int> frequency;
    for (int i = 0; i < N; i++) {
      frequency[nums[i]]++;

      int l = max(0, nums[i] - k);
      int r = min(maxi, nums[i] + k) + 1;

      difference[l]++;
      difference[r]--;

      difference[nums[i]] += 0;
    }

    int ans = 0;
    int cumSum = 0;
    for (auto it = difference.begin(); it != difference.end(); it++) {
      int candi = it->first;
      it->second += cumSum;

      int tfreq = frequency[candi];
      int convr = it->second - tfreq;

      int maxPossibleConvr = min(numOperations, convr);

      ans = max(ans, tfreq + maxPossibleConvr);

      cumSum = it->second;
    }

    return ans;

    // Complexity analysis 
    // Time : O(N * log(N)) + O(N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3347. Maximum Frequency of an Element After Performing Operations II - https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/description/?envType=daily-question&envId=2025-10-22 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 1,4,5 }, { 1, 2 } },
    { { 5,11,20,20 }, { 5, 1 } },
    { { 999999997,999999999,999999999 }, { 999999999, 2 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxFrequency(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

class Solution2 {
public:
  void nearlySorted(vector<int>& arr, int k) {
    // code here
    int N = arr.size();

    priority_queue<int, vector<int>, greater<int>> minHeap;

    for (int i = 0; i < k; i++) {
      minHeap.push(arr[i]);
    }

    int i = k;
    int j = 0;
    while (!minHeap.empty()) {
      if (i < N) minHeap.push(arr[i]);
      arr[j] = minHeap.top();
      minHeap.pop();
      i++;
      j++;
    }

    // Complexity analysis 
    // Time : O(N * Log(k)) 
    // Space : O(k) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Nearly sorted - https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1 

  vector<pair<vector<int>, int>> testcases = {
    { { 7, 9, 14 }, 1},
    { { 2, 3, 1, 4 }, 2},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    for (auto& e : tc.first) cout << e << " ";
    cout << endl;
    s2->nearlySorted(tc.first, tc.second);
    for (auto& e : tc.first) cout << e << " ";
    cout << endl;
    cout << endl;
  }
}

int main() {
  // Day 22 of October 2025

  p1();

  p2();

  return 0;
}
