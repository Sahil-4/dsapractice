#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  vector<char> vowelSet = { 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' };

  string solve1(string s) {
    vector<char> vowels;
    for (char& ch : s) {
      if (find(vowelSet.begin(), vowelSet.end(), ch) != vowelSet.end()) {
        vowels.push_back(ch);
      }
    }

    sort(vowels.begin(), vowels.end());

    string t;
    int vi = 0;
    for (char& ch : s) {
      if (find(vowelSet.begin(), vowelSet.end(), ch) != vowelSet.end()) {
        t.push_back(vowels[vi]);
        vi++;
      }
      else {
        t.push_back(ch);
      }
    }

    return t;

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) + O(N) 
    // Space : O(N) 
  }

  string solve2(string s) {
    vector<int> vowelsCount(10, 0);
    for (char& ch : s) {
      auto it = find(vowelSet.begin(), vowelSet.end(), ch);
      if (it != vowelSet.end()) {
        int ii = distance(vowelSet.begin(), it);
        vowelsCount[ii]++;
      }
    }

    string t;
    int vi = 0;
    for (char& ch : s) {
      if (find(vowelSet.begin(), vowelSet.end(), ch) != vowelSet.end()) {
        while (vowelsCount[vi] == 0) vi++;
        vowelsCount[vi]--;
        t.push_back(vowelSet[vi]);
      }
      else {
        t.push_back(ch);
      }
    }

    return t;

    // Complexity analysis 
    // Time : O(N) + O(N) 
    // Space : O(10) 
  }

public:
  string sortVowels(string s) {
    // s = "lEetcOde"
    // vowels = "EeOe"
    // vowelsSorted = "EOee"
    // t = "lEOtcede"

    // return solve1(s);
    return solve2(s);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2785. Sort Vowels in a String - https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11

  vector<string> testcases = { "lEetcOde","lYmpH" };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    cout << "INPUT: " << tc << endl;
    string out = s1->sortVowels(tc);
    cout << "OUTPUT: " << out << endl;
    cout << endl;
  }
}

class Solution2 {
private:
  int BOUND = (int)1e9;

  int recursion(vector<int>& nums, int N, int index) {
    if (index >= N - 1) return 0;

    int out = BOUND;
    int maxj = nums[index];

    for (int len = 1; len <= maxj; len++) {
      int jumps = 1 + recursion(nums, N, index + len);
      out = min(out, jumps);
    }

    return out;

    // Complexity analysis 
    // Time : O(N ^ N) 
    // Space : O(N) stack 
  }

  int memoize(vector<int>& nums, int N, int index, vector<int>& dp) {
    if (index >= N - 1) return 0;

    if (dp[index] != -1) return dp[index];

    int out = BOUND;
    int maxj = nums[index];

    for (int len = 1; len <= maxj; len++) {
      int jumps = 1 + memoize(nums, N, index + len, dp);
      out = min(out, jumps);
    }

    return dp[index] = out;

    // Complexity analysis 
    // Time : O(2 * N * N) 
    // Space : O(N) stack + O(N) memory 
  }

  int tabulation(vector<int>& nums, int N) {
    vector<int> dp(N + 1, 0);

    // base - handled 

    // recurrence 
    for (int index = N - 2; index >= 0; index--) {
      int out = BOUND;

      for (int len = 1; len <= nums[index]; len++) {
        int jumps = 1;
        if (index + len < N) jumps += dp[index + len];
        out = min(out, jumps);
      }

      dp[index] = out;
    }

    // return 
    return dp[0] < BOUND ? dp[0] : -1;

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(N) memory 
  }

  int greedy(vector<int>& nums, int N) {
    if (N <= 1) return 0;

    // greed criteira - chose farthest index from available window 

    int jumps = 0;

    // checkpoint - farthest i can reach 
    // reached - current index i reached 
    int checkpoint = 0, reached = 0;

    for (int i = 0; i < N; i++) {
      // extend the farthest window 
      checkpoint = max(checkpoint, i + nums[i]);

      if (i == reached) {
        reached = checkpoint;
        jumps++;
        if (checkpoint >= N - 1) break;
      }
    }

    return jumps;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }

  bool canReachEnd(vector<int>& arr, int N) {
    int maxReach = 0;

    for (int i = 0; i < N; i++) {
      if (i > maxReach) return false;
      maxReach = max(maxReach, i + arr[i]);
    }

    return true;
  }

public:
  int minJumps(vector<int>& nums) {
    // code here
    int N = nums.size();

    if (!canReachEnd(nums, N)) return -1;

    // return recursion(nums, N, 0);

    // vector<int> dp(N, -1);
    // return memoize(nums, N, 0, dp);

    // return tabulation(nums, N);

    return greedy(nums, N);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimum Jumps - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

  vector<vector<int>> testcases = {
    {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9},
    {1, 4, 3, 2, 6, 7},
    {0, 10, 20},
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    cout << "INPUT: ";
    for (auto e : tc) cout << e << " ";
    cout << endl;
    int out = s2->minJumps(tc);
    cout << "OUTPUT: " << out << endl;
    cout << endl;
  }
}

int main() {
  // Day 11 of September 2025

  p1();

  p2();

  return 0;
}
