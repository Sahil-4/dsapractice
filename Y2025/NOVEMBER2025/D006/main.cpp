#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  void dfs(vector<int>& vis, int node, vector<int> adj[], int par,
    unordered_map<int, set<int>>& mp, vector<int>& sPar) {
    vis[node] = 1;
    mp[par].insert(node);
    sPar[node] = par;

    for (auto child : adj[node]) {
      if (!vis[child]) {
        dfs(vis, child, adj, par, mp, sPar);
      }
    }
  }

  vector<int> processQueries(int c, vector<vector<int>>& connections,
    vector<vector<int>>& queries) {
    vector<int> adj[c + 1];

    for (auto i : connections) {
      int u = i[0];
      int v = i[1];

      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    unordered_map<int, set<int>> mp;
    vector<int> vis(c + 1, 0);
    vector<int> sPar(c + 1, 0);

    for (int i = 1; i <= c; i++) {
      if (!vis[i]) {
        dfs(vis, i, adj, i, mp, sPar);
      }
    }

    vector<int> ans;
    vector<int> online(c + 1, 1);

    for (auto i : queries) {
      int type = i[0];
      int node = i[1];

      int par = sPar[node];

      if (type == 2) {
        online[node] = 0;
        mp[par].erase(node);
      } else {
        if (online[node]) {
          ans.push_back(node);
        } else {
          if (mp[par].size() > 0) {
            ans.push_back(*mp[par].begin());
          } else {
            ans.push_back(-1);
          }
        }
      }
    }

    return ans;

    // Complexity Analysis
    // Time : O(N + Q*logN)
    // Space : O(N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3607. Power Grid Maintenance - https://leetcode.com/problems/power-grid-maintenance/description/?envType=daily-question&envId=2025-11-06 

  vector<pair<int, pair<vector<vector<int>>,
    vector<vector<int>>>>> testcases = {
    {
      5,
      {
        { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } },
        { { 1, 3 }, { 2, 1 }, { 1, 1 }, { 2, 2 }, { 1, 2 } }
      }
    },
    {
      3,
      {
        {},
        { { 1, 1 }, { 2, 1 }, { 1, 1 } }
      }
    },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<int> ans = s1->processQueries(tc.first, tc.second.first, tc.second.second);
    for (int a : ans) cout << a << endl;
  } cout << endl;
}

class Solution2 {
  int recursion(int n, vector<int>& memo) {
    if (n == 0) return 1;
    if (n < 0) return 0;

    if (memo[n] != -1) return memo[n];

    int c1 = recursion(n - 1, memo);
    int c2 = recursion(n - 2, memo);

    return memo[n] = (c1 + c2);

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) + O(N)
  }

  int tabulation(int N) {
    vector<int> memo(N + 1, -1);
    memo[0] = 1;
    memo[1] = 1;

    for (int n = 2; n <= N; n++) {
      int c1 = memo[n - 1];
      int c2 = memo[n - 2];

      memo[n] = (c1 + c2);
    }

    return memo[N];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }

  int optimised(int N) {
    int prev2 = 1;
    int prev1 = 1;
    int curr = 1;

    for (int n = 2; n <= N; n++) {
      curr = prev2 + prev1;
      prev2 = prev1;
      prev1 = curr;
    }

    return curr;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

public:
  int numberOfWays(int n) {
    // code here
    // if I place tile
    // vertically, then I move to (i + 1)
    // horizontally, then I move to (i + 2), and have to put two tiles (first, and second row)

    // vector<int> memo(n+1, -1);
    // return recursion(n, memo);

    // return tabulation(n);

    return optimised(n);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Ways To Tile A Floor - https://www.geeksforgeeks.org/problems/ways-to-tile-a-floor5836/1 

  vector<int> testcases = {
    1, 2, 3, 5, 7, 11, 13,
    15, 17, 23, 27, 35,
    37, 40, 45,
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->numberOfWays(tc) << endl;
  } cout << endl;
}

int main() {
  // Day 6 of November 2025

  p1();

  p2();

  return 0;
}
