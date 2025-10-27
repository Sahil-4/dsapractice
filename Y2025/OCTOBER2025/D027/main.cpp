#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int numberOfBeams(vector<string>& bank) {
    int R = bank.size();
    int C = bank[0].size();

    int beams = 0;
    int prevRow = 0;
    for (int ci = 0; ci < C; ci++) {
      prevRow += (bank[0][ci] - '0');
    }

    for (int ri = 1; ri < R; ri++) {
      int currRow = 0;
      for (int ci = 0; ci < C; ci++) {
        currRow += (bank[ri][ci] - '0');
      }

      if (currRow != 0) {
        beams += (prevRow * currRow);
        prevRow = currRow;
      }
    }

    return beams;

    // Complexity analysis
    // Time : O(R * C)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2125. Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-27 

  vector<vector<string>> testcases = {
    { "011001","000000","010100","001000" },
    { "000","111","000" },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->numberOfBeams(tc) << endl;
  }
}

class Solution2 {
public:
  vector<vector<int>> kSmallestPair(vector<int>& arr1, vector<int>& arr2, int k) {
    // code here
    // idea 
    // the very first pair will be (arr1[0] + arr2[0])
    // and the next pair will be either (arr1[1] + arr2[0]), arr1[0] + arr2[1]
    // hence if we have pair (arr1[i] + arr2[j]) 
    // and the next pair will be either (arr1[i + 1] + arr2[j]), arr1[i] + arr2[j + 1]

    int N = arr1.size();
    int M = arr2.size();

    vector<vector<int>> output;
    unordered_set<string> visited;
    // , vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

    pq.push({ arr1[0] + arr2[0], { 0, 0 } });
    visited.insert(to_string(0) + "." + to_string(0));

    while (k-- && !pq.empty()) {
      pair<int, pair<int, int>> pp = pq.top(); pq.pop();

      int sum = pp.first;
      int ci = pp.second.first;
      int cj = pp.second.second;

      output.push_back({ arr1[ci], arr2[cj] });

      if (ci + 1 < N && visited.find(to_string(ci + 1) + "." + to_string(cj)) == visited.end()) {
        pq.push({ arr1[ci + 1] + arr2[cj], { ci + 1, cj } });
        visited.insert(to_string(ci + 1) + "." + to_string(cj));
      }

      if (cj + 1 < M && visited.find(to_string(ci) + "." + to_string(cj + 1)) == visited.end()) {
        pq.push({ arr1[ci] + arr2[cj + 1], { ci, cj + 1 } });
        visited.insert(to_string(ci) + "." + to_string(cj + 1));
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(K* K*Log(K)) 
    // Space : O(K) + O(K) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Find K Smallest Sum Pairs - https://www.geeksforgeeks.org/problems/find-k-smallest-sum-pairs/1 

  vector<pair<pair<vector<int>, vector<int>>, int>> testcases = {
    { { { 1, 7, 11 }, { 2, 4, 6 } }, 3 },
    { { { 1, 3 }, { 2, 4 } }, 2 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<vector<int>> pairs = s2->kSmallestPair(tc.first.first, tc.first.second, tc.second);
    for (auto& pair : pairs) {
      cout << "[" << pair[0] << ", " << pair[1] << "]" << endl;
    } cout << endl;
  }
}

int main() {
  // Day 27 of October 2025

  p1();

  p2();

  return 0;
}
