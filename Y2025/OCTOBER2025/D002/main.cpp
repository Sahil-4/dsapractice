#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxBottlesDrunk(int numBottles, int numExchange) {
    int drunk = 0;

    while (numBottles >= numExchange) {
      drunk += numExchange;
      numBottles -= numExchange;
      numBottles += 1;
      numExchange++;
    }

    drunk += numBottles;

    return drunk;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3100. Water Bottles II - https://leetcode.com/problems/water-bottles-ii/description/?envType=daily-question&envId=2025-10-02 

  vector<pair<int, int>> testcases = { {1,2},{5,10},{9,3},{15,4},{100,99},{8,4},{100,2} };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxBottlesDrunk(tc.first, tc.second) << endl;
  }
}

class Solution2 {
private:
  void backtracking(vector<vector<int>>& combinations, int curr, vector<int>& combination, int left, int length) {
    if (left == 0 && combination.size() == length) {
      combinations.push_back(combination);
    }
    if (curr > 9 || left <= 0 || combination.size() >= length) {
      return;
    }

    // skip case 
    backtracking(combinations, curr + 1, combination, left, length);

    // take case 
    combination.push_back(curr);
    left -= curr;
    backtracking(combinations, curr + 1, combination, left, length);
    left += curr;
    combination.pop_back();

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(1)
  }

public:
  vector<vector<int>> combinationSum(int n, int k) {
    // code here
    // [1,2,3,4,5,6,7,8,9] 
    // fn(curr, comb, sum);

    vector<vector<int>> combinations;
    vector<int> combination;

    backtracking(combinations, 1, combination, n, k);

    return combinations;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Unique K-Number Sum - https://www.geeksforgeeks.org/problems/combination-sum-iii--111703/1 

  vector<pair<int, int>> testcases = { {9,3}, {3,3}, {1,1}, {50,9}, {40,9}, {40,8} };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<vector<int>> combinations = s2->combinationSum(tc.first, tc.second);
    for (auto& combination : combinations) {
      cout << "[ ";
      for (auto& num : combination) cout << num << " ";
      cout << "]";
      cout << endl;
    }
    cout << endl;
  }
}

int main() {
  // Day 2 of October 2025

  p1();

  p2();

  return 0;
}