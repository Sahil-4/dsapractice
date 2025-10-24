#include <bits/stdc++.h>

using namespace std;

// for pre-computation
set<int> balanced;
bool flag = true;

class Solution1 {
  void solve(set<string>& v, string s, int digit) {
    if (s.size() > 7 || digit > 7) {
      return;
    }

    if (s.size() > 0) {
      v.insert(s);
    }

    // skip
    solve(v, s, digit + 1);

    // pick
    string temp = s;
    for (int j = 1; j <= digit; j++) {
      temp += (digit + '0');
    }
    solve(v, temp, digit + 1);
  }

  void precompute() {
    set<string> v;

    solve(v, "", 1);

    for (string s : v) {
      string val = s;
      balanced.insert(stoi(s));
      while (next_permutation(val.begin(), val.end())) {
        balanced.insert(stoi(val));
      }
    }
  }

public:
  int nextBeautifulNumber(int n) {
    if (flag) {
      precompute();
      flag = false;
    }

    auto it = balanced.upper_bound(n);

    return *it;

    // Complexity analysis 
    // Time : O(Log(T)) 
    // Space : O(T) ~
    // T = 2^7
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2048. Next Greater Numerically Balanced Number - https://leetcode.com/problems/next-greater-numerically-balanced-number/description/?envType=daily-question&envId=2025-10-24 

  vector<int> testcases = { 1, 1000, 3000 };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->nextBeautifulNumber(tc) << endl;
  }
}

class Solution2 {
public:
  bool isPossible(vector<int>& arr, int k) {
      // code here
      priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq; // min heap 

      int N = arr.size();

      int index = 0;
      while (index < N) {
          if (pq.empty()) {
              pq.push({ arr[index], 1 });
              index++;
          } else {
              vector<int> top = pq.top();

              if (top[0] == arr[index]) {
                  pq.push({ arr[index], 1 });
                  index++;
              } else if (top[0] + 1 == arr[index]) {
                  pq.pop();
                  pq.push({ arr[index], top[1] + 1 });
                  index++;
              } else {
                  if (top[1] < k) return false;
                  else pq.pop();
              }
          }
      }

      while (!pq.empty()) {
          if (pq.top()[1] < k) return false;
          pq.pop();
      }

      return true;

      // Complexity analysis 
      // Time : O(N * Log(N)) 
      // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Split Array Subsequences - https://www.geeksforgeeks.org/problems/split-array-subsequences/1 

  vector<pair<vector<int>, int>> testcases = {
    { {2, 2, 3, 3, 4, 5}, 2 },
    { { 1, 1, 1, 1, 1 }, 4 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << (s2->isPossible(tc.first, tc.second) ? "true" : "false") << endl;
  }
}

int main() {
  // Day 24 of October 2025

  p1();

  p2();

  return 0;
}
