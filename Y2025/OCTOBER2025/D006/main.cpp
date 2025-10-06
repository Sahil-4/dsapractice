#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  vector<vector<int>> moves = { {-1, 0}, {0, +1}, {+1, 0}, {0, -1} };

  bool isValidIndex(int r, int c, int n) {
    return ((r >= 0 && r < n) && (c >= 0 && c < n));
  }

  bool dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int row, int col, int n, int time) {
    // cant move through this - required more time
    if (time < grid[row][col]) return false;

    // reached to destination - reached last cell
    if (row == n - 1 && col == n - 1) return true;

    // mark current cell visited
    visited[row][col] = true;

    // try moving in all 4 directions
    for (int i = 0; i < 4; i++) {
      int nrow = row + moves[i][0];
      int ncol = col + moves[i][1];

      // invalid index - cant go to this cell
      if (!isValidIndex(nrow, ncol, n)) continue;

      // already visited cell - no need to go to this cell
      if (visited[nrow][ncol]) continue;

      // move to [nrow][ncol] cell
      bool check = dfs(grid, visited, nrow, ncol, n, time);
      // return true if we can reach to last cell
      if (check) return true;
    }

    // unable to reach to last cell
    return false;
  }

public:
  int swimInWater(vector<vector<int>>& grid) {
    // --- binary search & DFS ---

    int n = grid.size();

    int low = 0;
    int high = n * n - 1;

    while (low < high) {
      int mid = low + ((high - low) / 2);

      vector<vector<bool>> visited(n, vector<bool>(n, false));

      bool check = dfs(grid, visited, 0, 0, n, mid);

      if (check) high = mid;
      else low = mid + 1;
    }

    return low;

    // Complexity analysis
    // Time : O(log(n*n) * (n*n))
    // Space : O(n*n) visited array + O(n + n) stack space
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 778. Swim in Rising Water - https://leetcode.com/problems/swim-in-rising-water/description/?envType=daily-question&envId=2025-10-06 

  vector<vector<vector<int>>> testcases = {
    { {0,2},{1,3} },
    { { 0,1,2,3,4 },{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6} },
    { { 26,99,80,1,89,86,54,90,47,87 },{9,59,61,49,14,55,77,3,83,79},{42,22,15,5,95,38,74,12,92,71},{58,40,64,62,24,85,30,6,96,52},{10,70,57,19,44,27,98,16,25,65},{13,0,76,32,29,45,28,69,53,41},{18,8,21,67,46,36,56,50,51,72},{39,78,48,63,68,91,34,4,11,31},{97,23,60,17,66,37,43,33,84,35},{75,88,82,20,7,73,2,94,93,81} },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->swimInWater(tc) << endl << endl;
  }
}

class Solution2 {
  vector<vector<int>> knightMoves = {
      {-2, -1}, {-2, +1},
      {-1, -2}, {-1, +2},
      {+1, -2}, {+1, +2},
      {+2, -1}, {+2, +1}
  };

  bool recursion(vector<vector<int>>& board, int crow, int ccol, int n, int steps) {
    if (steps == n * n - 1) {
      return true;
    }

    for (auto& move : knightMoves) {
      int nrow = crow + move[0];
      int ncol = ccol + move[1];

      if (nrow < 0 || nrow >= n || ncol < 0 || ncol >= n) continue;
      if (board[nrow][ncol] != -1) continue;

      board[nrow][ncol] = steps + 1;
      bool check = recursion(board, nrow, ncol, n, steps + 1);
      if (check) return true;
      board[nrow][ncol] = -1;
    }

    return false;
  }

public:
  vector<vector<int>> knightTour(int n) {
    // code here
    vector<vector<int>> invalid = { { -1 } };
    vector<vector<int>> board(n, vector<int>(n, -1));
    board[0][0] = 0;
    bool check = recursion(board, 0, 0, n, 0);

    return check ? board : invalid;

    // Complexity analysis 
    // Time : O(8^(n*n)) 
    // Space : O(n*n) + O(n*n) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks The Knight's tour problem - https://www.geeksforgeeks.org/problems/the-knights-tour-problem/1 

  vector<int> testcases = { 1,2,3,4,5,6 };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<vector<int>> moves = s2->knightTour(tc);
    for (auto& row : moves) {
      for (auto& col : row) {
        cout << col << " ";
      } cout << endl;
    } cout << endl;
  }
}

int main() {
  // Day 6 of October 2025

  p1();

  p2();

  return 0;
}
