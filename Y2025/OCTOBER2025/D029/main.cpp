#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int smallestNumber(int n) {
    int x = 1;

    while (x < n) {
      x = x << 1;
      x = x | 1;
    }

    return x;

    // Complexity analysis
    // Time : O(32)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3370. Smallest Number With All Set Bits - https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29 

  vector<int> testcases = { 5, 10, 3 };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->smallestNumber(tc) << endl;
  }
}

class Solution2 {
  pair<int, int> bfs(int start, vector<vector<int>>& graph) {
    vector<int> dist(graph.size(), -1);
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    int farthest = start;

    while (!q.empty()) {
      int u = q.front(); q.pop();
      for (int v : graph[u]) {
        if (dist[v] == -1) {
          dist[v] = dist[u] + 1;
          q.push(v);
          if (dist[v] > dist[farthest]) farthest = v;
        }
      }
    }
    return { farthest, dist[farthest] };
  }

public:
  int diameter(int V, vector<vector<int>>& edges) {
    vector<vector<int>> graph(V);
    for (auto& e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }

    auto [x, _] = bfs(0, graph);
    auto [y, diameter] = bfs(x, graph);
    return diameter;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Graph Diameter - https://www.geeksforgeeks.org/problems/diameter-of-a-graph/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    { 6, { {0, 1}, {0, 4}, {1, 3}, {1, 2}, {2, 5} } },
    { 7, { {0, 2}, {0, 4}, {0, 3}, {3, 1}, {3, 5}, {1, 6} } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->diameter(tc.first, tc.second) << endl;
  }
}

int main() {
  // Day 29 of October 2025

  p1();

  p2();

  return 0;
}
