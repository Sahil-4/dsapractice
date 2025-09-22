#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxFrequencyElements(vector<int>& nums) {
    int T = 101;

    int mfreq = 0;
    int mfreqCount = 1;

    vector<int> elementFrequency(T, 0);
    for (auto& num : nums) {
      int freq = ++elementFrequency[num];

      if (mfreq < freq) {
        mfreq = freq;
        mfreqCount = 1;
      } else if (mfreq == freq) {
        mfreqCount += 1;
      }
    }

    return mfreq * mfreqCount;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(T) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3005. Count Elements With Maximum Frequency - https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22 

  vector<vector<int>> testcases = {
    {1,2,2,3,1,4},
    {1,2,3,4,5},
    {15,2,41,2,3,4,3,1,41,2,3,4,55,3,1,41,2,3,4,3,1,41,2,3,4,5,2,3,1,5}
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxFrequencyElements(tc) << endl;
  }
}

class Solution2 {
private:
  vector<int> smaller(vector<int>& arr, int N, int initial, int start, int end, int inc) {
    vector<int> res(N, initial);

    stack<int> stk;
    stk.push(start);

    for (int i = start + inc; i != end; i += inc) {
      while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

      if (!stk.empty()) res[i] = stk.top();

      stk.push(i);
    }

    return res;
  }

public:
  vector<int> maxOfMins(vector<int>& arr) {
    // code here 

    int N = arr.size();
    vector<int> answer(N, 0);

    vector<int> leftSmaller = smaller(arr, N, -1, 0, N, +1);
    vector<int> rightSmaller = smaller(arr, N, N, N - 1, -1, -1);

    for (int i = 0; i < N; i++) {
      int wsize = rightSmaller[i] - leftSmaller[i] - 2;
      answer[wsize] = max(answer[wsize], arr[i]);
    }

    for (int i = N - 2; i >= 0; i--) {
      answer[i] = max(answer[i], answer[i + 1]);
    }

    return answer;

    // Complexity analysis 
    // Time : O(2N) + O(2N) 
    // Space : O(3N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Max of min for every window size - https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1 

  vector<vector<int>> testcases = {
    {10,20,30,50,10,70,30},
    {10,20,30},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> answer = s2->maxOfMins(tc);
    for (auto& e : answer) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 22 of September 2025

  p1();

  p2();

  return 0;
}
