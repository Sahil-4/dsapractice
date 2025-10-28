#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int isValid(vector<int> nums, int si, int dir) {
    int N = nums.size();

    int curr = si;
    while (curr >= 0 && curr < N) {
      if (nums[curr] > 0) {
        nums[curr] -= 1;
        dir *= -1;
      }

      curr += dir;
    }

    int flag = 1;
    for (int num : nums) {
      if (num != 0) {
        flag = 0;
        break;
      }
    }

    return flag;
  }

  int brute(vector<int>& nums) {
    int N = nums.size();

    int count = 0;
    for (int i = 0; i < N; i++) {
      if (nums[i] != 0) {
        continue;
      }

      count += isValid(nums, i, +1);
      count += isValid(nums, i, -1);
    }

    return count;

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(N)
  }

  int optimal(vector<int>& nums) {
    int N = nums.size();

    int count = 0;

    int leftSum = 0;
    int rightSum = 0;
    for (int num : nums) {
      rightSum += num;
    }

    for (int num : nums) {
      if (num == 0) {
        if (leftSum >= rightSum && leftSum - rightSum <= 1) {
          count += 1;
        }

        if (rightSum >= leftSum && rightSum - leftSum <= 1) {
          count += 1;
        }
      }

      leftSum += num;
      rightSum -= num;
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

public:
  int countValidSelections(vector<int>& nums) {
    // return brute(nums);
    return optimal(nums);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3354. Make Array Elements Equal to Zero - https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-28 

  vector<vector<int>> testcases = {
    {1,0,2,0,3},
    {2,3,4,0,4,1,0},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->countValidSelections(tc) << endl;
  }
}

class Solution2 {
  vector<vector<int>> dirs = { { -1, 0 }, { 0, +1 }, { +1, 0 }, { 0, -1 } };

  bool validIndex(int i, int j, int N, int M, vector<vector<bool>>& visited) {
    return (((i >= 0 && i < N) && (j >= 0 && j < M)) && visited[i][j] == false);
  }

public:
  vector<vector<int>> nearest(vector<vector<int>>& grid) {
    // code here
    int N = grid.size();
    int M = grid[0].size();

    vector<vector<bool>> visited(N, vector<bool>(M, false));
    vector<vector<int>> distance(N, vector<int>(M, 0));
    queue<vector<int>> que;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (grid[i][j] == 1) {
          visited[i][j] = true;
          que.push({ i, j, 0 });
        }
      }
    }

    while (!que.empty()) {
      vector<int> top = que.front(); que.pop();

      int ci = top[0];
      int cj = top[1];
      int cd = top[2];

      distance[ci][cj] = cd;

      for (auto dir : dirs) {
        int ni = ci + dir[0];
        int nj = cj + dir[1];

        if (!validIndex(ni, nj, N, M, visited)) continue;

        visited[ni][nj] = true;
        que.push({ ni, nj, cd + 1 });
      }
    }

    return distance;

    // Complexity analysis
    // Time : O(N * M * 2)
    // Space : O(N*M * 2)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Distance of nearest cell having 1 - https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1 

  vector<vector<vector<int>>> testcases = {
    {
      { 1, 0, 1 },
      { 1, 1, 0 },
      { 1, 0, 0 },
    },
    {
      { 0, 1, 1, 0 },
      { 1, 1, 0, 0 },
      { 0, 0, 1, 1 },
    },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<vector<int>> distance = s2->nearest(tc);
    for (auto r : distance) {
      for (auto c : r) {
        cout << c << " ";
      } cout << endl;
    } cout << endl;
  }
}

int main() {
  // Day 28 of October 2025

  p1();

  p2();

  return 0;
}
