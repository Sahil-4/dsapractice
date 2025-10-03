#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  typedef pair<int, pair<int, int>> PP;
  vector<vector<int>> directions = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 }, };

public:
  int trapRainWater(vector<vector<int>>& heightMap) {
    int m = heightMap.size();
    int n = heightMap[0].size();

    priority_queue<PP, vector<PP>, greater<>> boundary;
    vector<vector<bool>> visited(m, vector<bool>(n, false));

    // left & right most column 
    for (int r = 0; r < m; r++) {
      for (int c : { 0, n - 1 }) {
        boundary.push({ heightMap[r][c], { r, c } });
        visited[r][c] = true;
      }
    }

    // top & bottom most row 
    for (int c = 0; c < n; c++) {
      for (int r : { 0, m - 1 }) {
        boundary.push({ heightMap[r][c], { r, c } });
        visited[r][c] = true;
      }
    }

    int twater = 0;

    while (!boundary.empty()) {
      auto [height, cell] = boundary.top(); boundary.pop();
      int ri = cell.first;
      int ci = cell.second;

      for (auto& dir : directions) {
        int rj = ri + dir[0];
        int cj = ci + dir[1];

        // invalid cell 
        if (rj < 0 || cj < 0 || rj >= m || cj >= n) continue;
        // already visited 
        if (visited[rj][cj]) continue;

        // add water 
        twater += max(0, height - heightMap[rj][cj]);

        // push neighbour in pririty queue 
        boundary.push({ max(height, heightMap[rj][cj]), { rj, cj } });
        // mark visited 
        visited[rj][cj] = true;
      }
    }

    return twater;

    // Complexity analysis 
    // Time : O(MN * Log(MN)) 
    // Space : O(2MN) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 407. Trapping Rain Water II - https://leetcode.com/problems/trapping-rain-water-ii/description/?envType=daily-question&envId=2025-10-03 

  vector<vector<vector<int>>> testcases = {
    { { 1,4,3,1,3,2 },{ 3,2,1,3,2,4 },{ 2,3,3,2,3,1 } },
    { { 3,3,3,3,3 },{ 3,2,2,2,3 },{ 3,2,1,2,3 },{ 3,2,2,2,3 },{ 3,3,3,3,3 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->trapRainWater(tc) << endl;
  }
}

class Solution2 {
private:
  vector<vector<char>> keypad = {
      {},
      {}, { 'a', 'b', 'c' }, { 'd', 'e', 'f' },
      { 'g', 'h', 'i' }, { 'j', 'k', 'l' }, { 'm', 'n', 'o' },
      { 'p', 'q', 'r', 's' }, { 't', 'u', 'v' }, { 'w', 'x', 'y', 'z' },
  };

  void solve(vector<string>& words, vector<int>& arr, int N, int cindex, string& word) {
    if (cindex >= N) {
      words.push_back(word);
      return;
    }
    if (arr[cindex] == 0 || arr[cindex] == 1) return solve(words, arr, N, cindex + 1, word);

    for (char ch : keypad[arr[cindex]]) {
      word.push_back(ch);
      solve(words, arr, N, cindex + 1, word);
      word.pop_back();
    }

    // Complexity analysis 
    // Time : O(4^N) 
    // Space : O(N) + O(N) 
  }

public:
  vector<string> possibleWords(vector<int>& arr) {
    // code here
    vector<string> words;
    string word;
    int N = arr.size();

    solve(words, arr, N, 0, word);

    return words;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Possible Words From Phone Digits - https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1 

  vector<vector<int>> testcases = {
    {1},
    {2},
    {2,3},
    {2,3,4},
    {4,4,4},
    {7,7,7},
    {2,4,5,6,1,3,7,8,9},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<string> words = s2->possibleWords(tc);
    for (string& word : words) cout << word << endl;
    cout << endl;
  }
}

int main() {
  // Day 3 of October 2025

  p1();

  p2();

  return 0;
}
