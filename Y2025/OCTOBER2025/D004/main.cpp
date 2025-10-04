#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxArea(vector<int>& height) {
    // using two pointers 

    int marea = 0;

    int N = height.size();

    int l = 0;
    int r = N - 1;

    while (l < r) {
      // height of left, right lines 
      int x = height[l];
      int y = height[r];

      // update answer 
      int area = min(x, y) * (r - l);
      marea = max(marea, area);

      // update pointers 
      if (x < y) l++;
      else r--;
    }

    return marea;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 11. Container With Most Water - https://leetcode.com/problems/container-with-most-water/description/?envType=daily-question&envId=2025-10-04 

  vector<vector<int>> testcases = {
    {1,8,6,2,5,4,8,3,7},
    {1,1},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxArea(tc) << endl;
  }
}

class Solution2 {
private:
  void solve(vector<string>& expressions, string expression, long long cresult, long long presult, int target, string& str, int curr_index) {
    int N = str.length();

    if (curr_index == N) {
      if (cresult == target) expressions.push_back(expression);
      return;
    }

    for (int i = curr_index; i < N; i++) {
      if (i > curr_index && str[curr_index] == '0') return;

      string sub = str.substr(curr_index, i - curr_index + 1);
      long long curr_number = stoll(sub);

      if (curr_index == 0) {
        solve(expressions, expression + sub, cresult + curr_number, curr_number, target, str, i + 1);
      } else {
        solve(expressions, expression + "+" + sub, cresult + curr_number, curr_number, target, str, i + 1);
        solve(expressions, expression + "-" + sub, cresult - curr_number, -curr_number, target, str, i + 1);
        solve(expressions, expression + "*" + sub, (cresult - presult) + (presult * curr_number), presult * curr_number, target, str, i + 1);
      }
    }
  }

public:
  vector<string> findExpr(string& s, int target) {
    // code here
    vector<string> expressions;
    string expression = "";
    solve(expressions, expression, 0, 0, target, s, 0);

    return expressions;

    // Complexity analysis 
    // Time : O(N^N) 
    // Space : O(N) stack + O(N) hold expression
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Expression Add Operators - https://www.geeksforgeeks.org/problems/expression-add-operators/1 

  vector<pair<string, int>> testcases = {
    {"125", 7},
    {"124", 9},
    {"12", 12},
    {"987612", 200},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<string> expressions = s2->findExpr(tc.first, tc.second);
    cout << "[" << endl;
    for (string& expression : expressions) cout << "  " << expression << endl;
    cout << "]" << endl;
  }
}

int main() {
  // Day 4 of October 2025

  p1();

  p2();

  return 0;
}
