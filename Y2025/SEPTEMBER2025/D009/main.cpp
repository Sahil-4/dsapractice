#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int peopleAwareOfSecret(int n, int delay, int forget) {
    // using dp
    // dp[i] = aware + dp[i - delay] - dp[i - forget]

    long long MOD = 1e9 + 7;
    long long ans = 0;

    long long aware = 0;
    vector<long long> dp(n);
    dp[0] = 1; // on day 1, only 1 people knows secret

    for (int i = 1; i < n; i++) {
      if (i >= delay) {
        aware = ((aware + dp[i - delay]) % MOD);
      }
      if (i >= forget) {
        aware = ((aware - dp[i - forget] + MOD) % MOD);
      }

      dp[i] = aware;
    }

    for (int i = n - forget; i < n; i++) {
      ans = ((ans + dp[i]) % MOD);
    }

    return ans;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2327. Number of People Aware of a Secret - https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09

  vector<vector<int>> testcases = {
    {6, 2, 4},
    {4, 1, 3},
    {1000, 1, 1000},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << "INPUT: " << tc[0] << " " << tc[1] << " " << tc[2] << endl;
    int out = s1->peopleAwareOfSecret(tc[0], tc[1], tc[2]);
    cout << "OUTPUT: " << out << endl << endl;
  }
}

class Solution2 {
public:
  int assignHole(vector<int>& mices, vector<int>& holes) {
    // code here
    // mices[] = [4, -4, 2], holes[] = [4, 0, 5] 
    // mices[] = [-4, 2, 4], holes[] = [0, 4, 5] 
    // mices[] = [1, 2], holes[] = [20, 10] 
    // mices[] = [1, 2], holes[] = [10, 20] 
    // sort both arrays ASC 
    // use two pointers mi (for mices array), hi (for holes array) 
    // sorting make sure the mices and holes on index i are closest 
    // we just have to find the max diff between mices[i] and holes[i] 

    sort(mices.begin(), mices.end());
    sort(holes.begin(), holes.end());

    int N = mices.size();

    int maxDiff = 0;

    for (int i = 0; i < N; i++) {
      int diff = abs(mices[i] - holes[i]);
      maxDiff = max(maxDiff, diff);
    }

    return maxDiff;

    // Complexity analysis 
    // Time : O(2 * N * Log(N)) + O(N) 
    // Space : O(2 * N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Assign Mice Holes - https://www.geeksforgeeks.org/problems/assign-mice-holes3053/1

  vector<pair<vector<int>, vector<int>>> testcases = {
    {
      {4, -4, 2},
      {4, 0, 5},
    },
    {
      {1, 2},
      {20, 10},
    },
    {
      {2, 5, 54, 8, 9, 5, 4, 15, 14},
      {2, 5, 54, 8, 9, 5, 4, 15, 14},
    },
    {
      {2, 5, 54, 8, 9, 5, 4, 15, 14},
      {12, 15, 154, 18, 91, 51, 14, 115, 141},
    },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT: " << endl;
    for (int m : tc.first) cout << m << " ";
    cout << endl;
    for (int h : tc.second) cout << h << " ";
    cout << endl;

    int out = s2->assignHole(tc.first, tc.second);
    cout << "OUTPUT: " << endl << out << endl << endl;
  }
}

int main() {
  // Day 9 of September 2025

  p1();

  p2();

  return 0;
}
