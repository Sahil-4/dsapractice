#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int minNumberOperations(vector<int>& target) {
    // target  = [1,2,3,2,1]
    // initial = [1,2,3,2,1]
    // opr = 3 
    // target  = [3,1,1,2]
    // initial = [3,1,1,2]
    // opr = 4

    int N = target.size();

    int opr = target[0];
    for (int i = 0; i < N - 1; i++) {
      if (target[i + 1] > target[i]) {
        opr += (target[i + 1] - target[i]);
      }
    }

    return opr;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1526. Minimum Number of Increments on Subarrays to Form a Target Array - https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/?envType=daily-question&envId=2025-10-30 

  vector<vector<int>> testcases = {
    { 1,2,3,2,1 },
    { 3,1,1,2 },
    { 3,1,5,4,2 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minNumberOperations(tc) << endl;
  }
}

class Solution2 {
  vector<vector<int>> dirs = { {-1, 0}, {0, +1}, {+1, 0}, {0, -1} };

  void markUnreachable(int ri, int ci, vector<vector<char>>& grid) {
    int RN = grid.size();
    int CN = grid[0].size();

    grid[ri][ci] = '.';

    for (auto dir : dirs) {
      int nri = ri + dir[0];
      int nci = ci + dir[1];

      if (nri < 0 || nri >= RN || nci < 0 || nci >= CN) continue;
      if (grid[nri][nci] != 'O') continue;

      markUnreachable(nri, nci, grid);
    }
  }

public:
  void fill(vector<vector<char>>& grid) {
    // Code here

    int RN = grid.size();
    int CN = grid[0].size();

    for (int ri = 0; ri < RN; ri++) {
      if (grid[ri][0] == 'O') {
        markUnreachable(ri, 0, grid);
      }
      if (grid[ri][CN - 1] == 'O') {
        markUnreachable(ri, CN - 1, grid);
      }
    }

    for (int ci = 0; ci < CN; ci++) {
      if (grid[0][ci] == 'O') {
        markUnreachable(0, ci, grid);
      }
      if (grid[RN - 1][ci] == 'O') {
        markUnreachable(RN - 1, ci, grid);
      }
    }

    for (int ri = 0; ri < RN; ri++) {
      for (int ci = 0; ci < CN; ci++) {
        if (grid[ri][ci] == 'O') {
          grid[ri][ci] = 'X';
        } else if (grid[ri][ci] == '.') {
          grid[ri][ci] = 'O';
        }
      }
    }

    // Complexity analysis
    // Time : O(N * (N + M)) + O(M * (N + M)) + O(N * M)
    // Space : O(1)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Replace O's with X's - https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1 

  vector<vector<vector<char>>> testcases = {
    {
      {'X', 'X', 'X', 'X'},
      {'X', 'O', 'X', 'X'},
      {'X', 'O', 'O', 'X'},
      {'X', 'O', 'X', 'X'},
      {'X', 'X', 'O', 'O'}
    },
    {
      {'X', 'O', 'X', 'X'},
      {'X', 'O', 'X', 'X'},
      {'X', 'O', 'O', 'X'},
      {'X', 'O', 'X', 'X'},
      {'X', 'X', 'O', 'O'}
    },
    {
      {'X', 'X', 'X'},
      {'X', 'O', 'X'},
      {'X', 'X', 'X'}
    },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    int n = tc.size();
    int m = tc[0].size();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cout << tc[i][j] << " ";
      } cout << endl;
    } cout << "-->" << endl;
    s2->fill(tc);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cout << tc[i][j] << " ";
      } cout << endl;
    } cout << endl;
  }
}

int main() {
  // Day 30 of October 2025

  p1();

  p2();

  return 0;
}
