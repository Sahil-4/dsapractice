#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxFrequency(vector<int>& nums, int k, int numOperations) {
    int mini = *min_element(nums.begin(), nums.end());
    int maxi = *max_element(nums.begin(), nums.end());

    vector<int> frequency(maxi + 1, 0);
    for (int e : nums) {
      frequency[e]++;
    }
    for (int e = 1; e <= maxi; e++) {
      frequency[e] += frequency[e - 1];
    }

    int ans = 0;
    for (int candi = mini; candi <= maxi; candi++) {
      int l = max(mini, candi - k);
      int r = min(maxi, candi + k);

      int fcandi = frequency[candi] - frequency[candi - 1];
      int extra = min(numOperations, frequency[r] - frequency[l - 1] - fcandi);
      int freq = fcandi + extra;

      ans = max(ans, freq);
    }

    return ans;

    // Complexity analysis 
    // Time : O(N) + O(2M) 
    // Space : O(M) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3346. Maximum Frequency of an Element After Performing Operations I - https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/?envType=daily-question&envId=2025-10-21 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 1,4,5 }, { 1, 2 } },
    { { 5,11,20,20 }, { 5, 1 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxFrequency(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

class Solution2 {
public:
  vector<int> topKFreq(vector<int>& arr, int k) {
    // Code here
    unordered_map<int, int> frequency;

    for (int e : arr) frequency[e]++;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (auto it : frequency) {
      int e = it.first;
      int f = it.second;

      pq.push({ f, e });

      if (pq.size() > k) pq.pop();
    }

    vector<int> output;
    while (!pq.empty()) {
      int f = pq.top().first;
      int e = pq.top().second;
      pq.pop();

      output.push_back(e);
    }

    reverse(output.begin(), output.end());

    return output;

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) + O(N) 
    // Space : O(N) + O(N) 
    // in worst case K = N
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Top K Frequent in Array - https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1 

  vector<pair<vector<int>, int>> testcases = {
    { { 3, 1, 4, 4, 5, 2, 6, 1 }, 2 },
    { { 7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9 }, 4 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> topK = s2->topKFreq(tc.first, tc.second);
    for (int e : topK) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 21 of October 2025

  p1();

  p2();

  return 0;
}
