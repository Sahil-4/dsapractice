#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
    vector<vector<int>> grid(m, vector<int>(n, 0));

    for (auto& blockage : guards) {
      grid[blockage[0]][blockage[1]] = 1;
    }

    for (auto& blockage : walls) {
      grid[blockage[0]][blockage[1]] = 1;
    }

    for (auto& guard : guards) {
      int r, c;

      // north
      r = guard[0] - 1;
      c = guard[1];
      while (r >= 0 && grid[r][c] != 1) {
        grid[r][c] = 2;
        r--;
      }

      // east
      r = guard[0];
      c = guard[1] + 1;
      while (c < n && grid[r][c] != 1) {
        grid[r][c] = 2;
        c++;
      }

      // south
      r = guard[0] + 1;
      c = guard[1];
      while (r < m && grid[r][c] != 1) {
        grid[r][c] = 2;
        r++;
      }

      // west
      r = guard[0];
      c = guard[1] - 1;
      while (c >= 0 && grid[r][c] != 1) {
        grid[r][c] = 2;
        c--;
      }
    }

    int count = 0;
    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        count += (grid[r][c] == 0);
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(4 * m * n)
    // Space : O(m * n)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2257. Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2025-11-02 

  vector<pair<pair<int, int>, pair<vector<vector<int>>, vector<vector<int>>>>> testcases = {
    { { 4, 6 }, { {{0,0},{1,1},{2,3}}, {{0,1},{2,2},{1,4}} } },
    { { 3, 3 }, { {{1,1}}, {{0,1},{1,0},{2,1},{1,2}} } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->countUnguarded(tc.first.first, tc.first.second, tc.second.first, tc.second.second) << endl;
  }
}

class Solution2 {
public:
  int maxEdgesToAdd(int V, vector<vector<int>>& edges) {
    // code here
    int totalPossibleEdges = ((V - 1) * V) / 2;
    int currentEdges = edges.size();
    int remainingEdges = totalPossibleEdges - currentEdges;
    return remainingEdges;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Max DAG Edges - https://www.geeksforgeeks.org/problems/max-dag-edges/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    {3, {{0, 1}, {1, 2}}},
    {4, {{0, 1}, {0, 2}, {1, 2}, {2, 3}}},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->maxEdgesToAdd(tc.first, tc.second) << endl;
  }
}

int main() {
  // Day 2 of November 2025

  p1();

  p2();

  return 0;
}
