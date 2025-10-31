#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  vector<int> getSneakyNumbers(vector<int>& nums) {
    // nums = [0,3,2,1,3,2]
    // n = 4
    // nums = [.4,.7,.6,.5,3,2]

    int n = nums.size() - 2;
    vector<int> sneakyNumbers;

    for (int e : nums) {
      int index = e % n;

      if (nums[index] >= n) {
        sneakyNumbers.push_back(index);
      } else {
        nums[index] += n;
      }
    }

    // fix the input again
    for (int i = 0; i < nums.size(); i++) {
      nums[i] = nums[i] % n;
    }

    return sneakyNumbers;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3289. The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-31 

  vector<vector<int>> testcases = {
    {0,1,1,0},
    {0,3,2,1,3,2},
    {7,1,5,4,3,4,6,0,9,5,8,2},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<int> sneakyNumbers = s1->getSneakyNumbers(tc);
    cout << "[ " << sneakyNumbers[0] << ", " << sneakyNumbers[1] << " ]" << endl;
  }
}

class Solution2 {
  int cycleLength(vector<vector<int>>& adj, int source, int V) {
    int ans = INT_MAX;

    vector<bool> visited(V, false);
    vector<int> dist(V, INT_MAX);
    queue<vector<int>> bfs;

    visited[source] = true;
    dist[source] = 0;
    bfs.push({ source, -1, 0 });

    while (!bfs.empty()) {
      vector<int> vertex = bfs.front(); bfs.pop();

      int u = vertex[0];
      int p = vertex[1];
      int l = vertex[2];

      for (int n : adj[u]) {
        if (n == p) continue;

        if (!visited[n]) {
          visited[n] = true;
          dist[n] = l + 1;
          bfs.push({ n, u, l + 1 });
        } else {
          int cycle_len = dist[u] + dist[n] + 1;
          ans = min(ans, cycle_len);
        }
      }
    }

    return ans;
  }

public:
  int shortCycle(int V, vector<vector<int>>& edges) {
    // Code here
    // length of shortest cycle
    int min_cycle = INT_MAX;

    // build adjacency list
    vector<vector<int>> adj(V, vector<int>());
    for (vector<int>& edge : edges) {
      int u = edge[0], v = edge[1];

      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    for (int src = 0; src < V; src++) {
      int cycle = cycleLength(adj, src, V);
      min_cycle = min(min_cycle, cycle);
    }

    return min_cycle == INT_MAX ? -1 : min_cycle;

    // Complexity analysis
    // Time : O(E) + O(V * (V + E))
    // Space : O(V + E) + O(V) + O(V) + O(E)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Shortest Cycle - https://www.geeksforgeeks.org/problems/shortest-cycle/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    { 7, { {0, 5}, {0, 6}, {5, 1}, {6, 1}, {6, 2}, {2, 3}, {3, 4}, {1, 4} } },
    { 7, { {0, 5}, {0, 6}, {1, 2}, {1, 4}, {1, 5}, {1, 6}, {2, 6}, {2, 3}, {3, 4} } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->shortCycle(tc.first, tc.second) << endl;
  }
}

int main() {
  // Day 31 of October 2025

  p1();

  p2();

  return 0;
}
