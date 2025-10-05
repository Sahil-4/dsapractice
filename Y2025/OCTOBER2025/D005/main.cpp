#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  typedef pair<char, pair<int, int>> PP;
  vector<PP> dirsRules = {
      {'U', {-1, 0}}, {'D', {1, 0}}, {'L', {0, -1}}, {'R', {0, 1}}
  };

  vector<vector<bool>> canReach(vector<vector<int>>& heights, int m, int n, int to) {
    vector<vector<bool>> reach(m, vector<bool>(n, false));
    queue<pair<int, int>> bfsQue;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (to == -1 && (i == 0 || j == 0)) {
          bfsQue.push({ i, j });
          reach[i][j] = true;
        }
        if (to == +1 && (i == m - 1 || j == n - 1)) {
          bfsQue.push({ i, j });
          reach[i][j] = true;
        }
      }
    }

    while (!bfsQue.empty()) {
      int ci = bfsQue.front().first;
      int cj = bfsQue.front().second;
      bfsQue.pop();

      for (auto& dirsRule : dirsRules) {
        int ni = ci + dirsRule.second.first;
        int nj = cj + dirsRule.second.second;

        if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
        if (heights[ni][nj] < heights[ci][cj]) continue;
        if (reach[ni][nj]) continue;

        bfsQue.push({ ni, nj });
        reach[ni][nj] = true;
      }
    }

    return reach;
  }

public:
  vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
    int m = heights.size();
    int n = heights[0].size();

    vector<vector<bool>> P = canReach(heights, m, n, -1);
    vector<vector<bool>> A = canReach(heights, m, n, +1);

    vector<vector<int>> PA;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (P[i][j] && A[i][j]) PA.push_back({ i, j });
      }
    }

    return PA;

    // Complexity analysis 
    // Time : O(M*N) 
    // Space : O(M*N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 417. Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05 

  vector<vector<vector<int>>> testcases = {
    { {1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4} },
    { { 1 } },
    { { 19,16,16,12,14,0,17,11,2,0,18,9,13,16,8,8,8,13,17,9,16,9,4,7,1,19,10,7,0,15 },{0,11,4,14,9,0,6,13,16,5,19,9,4,5,4,12,0,13,0,7,9,12,13,15,3,7,4,9,15,1},{13,14,12,12,12,16,6,15,13,1,8,9,11,14,14,10,19,11,10,0,5,18,4,12,7,13,17,15,18,1},{16,14,19,5,8,2,11,17,7,1,4,6,5,18,7,15,6,19,18,12,1,14,2,2,0,9,15,14,13,19},{17,4,12,9,12,10,12,10,4,5,12,7,2,12,18,10,10,8,6,1,5,13,10,3,5,3,11,4,8,11},{8,19,18,9,6,2,7,3,19,6,0,17,9,12,11,1,15,11,18,1,8,11,1,11,16,7,8,17,15,0},{7,0,5,11,1,7,12,18,12,1,5,2,11,7,18,12,0,11,9,18,5,2,3,1,1,1,8,14,19,5},{2,14,2,16,17,19,10,16,1,16,16,3,19,12,13,17,19,12,16,10,16,8,16,12,6,12,13,17,9,12},{8,1,10,5,7,0,15,19,8,15,4,12,18,18,13,11,5,2,8,3,15,4,3,7,7,14,15,11,6,16},{0,5,13,19,1,1,2,4,16,2,16,9,15,15,10,10,18,11,17,1,5,14,5,19,7,0,13,7,13,7},{11,6,16,12,4,2,9,11,17,19,12,10,6,16,17,5,1,18,19,7,15,1,14,0,3,19,7,3,4,13},{4,11,8,10,10,19,7,18,4,2,2,14,6,9,18,14,2,16,5,3,19,17,4,3,7,1,12,2,4,3},{14,16,3,11,13,13,6,16,18,0,17,19,4,1,14,12,4,17,5,19,8,13,15,3,15,4,1,14,12,10},{13,2,12,2,16,12,19,10,19,12,19,14,12,17,16,3,13,7,3,15,16,7,10,15,14,10,6,5,2,18} },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<vector<int>> PA = s1->pacificAtlantic(tc);
    for (auto& pa : PA) {
      cout << pa[0] << " " << pa[1] << endl;
    }
    cout << endl;
  }
}

class Solution2 {
private:
  typedef pair<char, pair<int, int>> PP;
  vector<PP> dirsRules = { {'U', {-1, 0}}, {'D', {1, 0}}, {'L', {0, -1}}, {'R', {0, 1}} };

  void recursion(vector<string>& paths, string& path, vector<vector<int>>& maze, int cr, int cc, vector<vector<bool>>& visited) {
    int N = maze.size();
    if (cr == N - 1 && cc == N - 1) {
      paths.push_back(path);
      return;
    }
    if (cr < 0 || cc < 0 || cr >= N || cc >= N) return;
    if (visited[cr][cc]) return;
    if (maze[cr][cc] == 0) return;

    visited[cr][cc] = true;

    for (auto& dirsRule : dirsRules) {
      char dir = dirsRule.first;
      int ruleR = dirsRule.second.first;
      int ruleC = dirsRule.second.second;

      path.push_back(dir);
      cr += ruleR;
      cc += ruleC;

      recursion(paths, path, maze, cr, cc, visited);

      cc -= ruleC;
      cr -= ruleR;
      path.pop_back();
    }

    visited[cr][cc] = false;
  }

public:
  vector<string> ratInMaze(vector<vector<int>>& maze) {
    // code here
    int N = maze.size();

    // starting cell is blocked 
    if (maze[0][0] == 0) return {};
    // destination cell is blocked 
    if (maze[N - 1][N - 1] == 0) return {};

    vector<string> paths;
    string path = "";
    vector<vector<bool>> visited(N, vector<bool>(N, false));

    recursion(paths, path, maze, 0, 0, visited);

    sort(paths.begin(), paths.end());

    return paths;

    // Complexity analysis 
    // Time : O(4^N) 
    // Space : O(N * N) + O(N) + O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Rat in a Maze - https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1 

  vector<vector<vector<int>>> testcases = {
    { {1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1} },
    { { 1, 0 }, {1, 0} },
    { { 1, 1, 1 }, {1, 0, 1}, {1, 1, 1} },
    { { 1, 1, 1, 0, 1 }, {1, 0, 1, 1, 1}, {0, 0, 1, 1, 1}, {1, 0, 0, 1, 1}, {1, 0, 0, 0, 1} },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<string> paths = s2->ratInMaze(tc);
    for (string& path : paths) cout << path << endl;
    cout << endl;
  }
}

int main() {
  // Day 5 of October 2025

  p1();

  p2();

  return 0;
}
