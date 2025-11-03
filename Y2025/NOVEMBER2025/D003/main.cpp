#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int minCost(string colors, vector<int>& neededTime) {
    int N = colors.size();

    int tcost = 0;

    int prev = 0;
    int curr = 1;

    while (curr < N) {
      if (colors[curr] != colors[prev]) {
        prev = curr;
      } else {
        if (neededTime[prev] <= neededTime[curr]) {
          // delete prev
          tcost += neededTime[prev];
          prev = curr;
        } else {
          // delete curr
          tcost += neededTime[curr];
          prev = prev;
        }
      }

      curr++;
    }

    return tcost;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1578. Minimum Time to Make Rope Colorful - https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/?envType=daily-question&envId=2025-11-03 

  vector<pair<string, vector<int>>> testcases = {
    { "abaac", { 1,2,3,4,5 } },
    { "abc", { 1,2,3 } },
    { "aabaa", { 1,2,3,4,1 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minCost(tc.first, tc.second) << endl;
  }
}

class Solution2 {
public:
  vector<int> safeNodes(int V, vector<vector<int>>& edges) {
    // Code here
    // create a reverse adjacency list
    // and outdegree array
    // using topo sort
    // start from nodes with outdegree == 0
    // visit node v from u
    // and keep decresing outdegree
    // if at any point outdegree == 0
    // put it into bfs que 
    // upon popping it from que add node to snodes for output

    vector<int> snodes;

    vector<vector<int>> radj(V, vector<int>());
    vector<int> outdegree(V, 0);
    for (auto& edge : edges) {
      int u = edge[0];
      int v = edge[1];

      radj[v].push_back(u);
      outdegree[u]++;
    }

    queue<int> que;

    for (int i = 0; i < V; i++) {
      if (outdegree[i] == 0) {
        que.push(i);
      }
    }

    while (!que.empty()) {
      int node = que.front(); que.pop();

      snodes.push_back(node);

      for (int neighbour : radj[node]) {
        outdegree[neighbour]--;
        if (outdegree[neighbour] == 0) {
          que.push(neighbour);
        }
      }
    }

    return snodes;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Safe States - https://www.geeksforgeeks.org/problems/eventual-safe-states/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    { 4, { {1, 2}, {2, 3}, {3, 2} } },
    { 5, { {1, 0}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {3, 4} } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> snodes = s2->safeNodes(tc.first, tc.second);
    cout << "[ ";
    for (int node : snodes) cout << node << " ";
    cout << "]";
    cout << endl;
  }
}

int main() {
  // Day 3 of November 2025

  p1();

  p2();

  return 0;
}
