#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int solve1(int numBottles, int numExchange) {
    // bottles consumed
    int consumed = 0;

    // simulate process
    while (numBottles >= numExchange) {
      // slow simulation
      consumed += numExchange;
      numBottles -= numExchange;
      numBottles += 1;
    }

    // add left over bottles
    consumed += numBottles;

    // return count of bottles consumed
    return consumed;

    // Complexity analysis
    // Time : O(numBottles)
    // Space : O(1)
  }

  int solve2(int numBottles, int numExchange) {
    // bottles consumed
    int consumed = 0;

    // simulate process
    while (numBottles >= numExchange) {
      // fast simulation
      int leftOver = (numBottles % numExchange); // cant take in set
      int willConsume = numBottles - leftOver; // total bottles in all sets
      int newBottles = numBottles / numExchange; // bottles got from exchange
      int currBottles = newBottles + leftOver; // bottles left with

      // update
      consumed += willConsume;
      numBottles = currBottles;
    }

    // add left over bottles
    consumed += numBottles;

    // return count of bottles consumed
    return consumed;

    // Complexity analysis
    // Time : O(Log_numExchange(numBottles))
    // Space : O(1)
  }

  int solve3(int numBottles, int numExchange) {
    // Steps to reach to final O(1) solution
    // Step 1: Think about total bottles
    // At the start you have numBottles 
    // and you’ll definitely drink all of them. 
    // So whatever formula you build, the result is going to be:
    // consumed = numBottles + (extra bottles gained by exchanging)
    // Step 2: Track just the exchanges
    // Forget drinking for a moment.
    // Focus only on: “How many extra bottles can I get by repeatedly exchanging?”
    // Step 3: Small examples to see patterns
    // Try manually with different (numBottles, numExchange) pairs:
    // Case 1: numBottles=9, numExchange=3
    // You’ll drink 9 initially.
    // From 9 empties → 3 exchanges → 3 more bottles.
    // From those 3 empties → 1 exchange → 1 more bottle.
    // Total = 9 + 3 + 1 = 13.
    // Notice: extra = 4, which is (9 - 1) / (3 - 1)
    // Case 2: numBottles=15, numExchange=4
    // Drink 15.
    // Exchanges: 15 empties → 3 new bottles (with leftover 3).
    // Then 6 empties → 1 new bottle (with leftover 2).
    // … and so on.
    // Eventually, total = 19.
    // Extra = 4, which matches (15 - 1) / (4 - 1)
    // Step 4: Pattern
    // The extra bottles gained always looks like:
    // extra = (numBottles - 1) / (numExchange - 1)
    // Why? Because every exchange cycle effectively “burns” (numExchange - 1) bottles into 1 new drink.
    // Step 5: Final relation
    // So your formula becomes:
    // consumed = numBottles + extra

    int extra = (numBottles - 1) / (numExchange - 1);
    int consumed = numBottles + extra;

    return consumed;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

public:
  int numWaterBottles(int numBottles, int numExchange) {
    // numBottles = 15, numExchange = 4
    // consume in set of numExchange = 4
    // numBottles = 15, numExchange = 4
    // (numBottles >= numExchange)
    // we can consume numExchange and get 1 from market
    // numBottles = numBottles - numExchange + 1;
    // numBottles = 12
    // (numBottles >= numExchange)
    // again we can consume numExchange and get 1 from market
    // numBottles = numBottles - numExchange + 1;
    // numBottles = 12
    // numBottles = numBottles - numExchange + 1;
    // numBottles = 9
    // we will do this till (numBottles >= numExchange)
    // and count all bottles we consumed

    // return solve1(numBottles, numExchange);
    // return solve2(numBottles, numExchange);
    return solve3(numBottles, numExchange);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1518. Water Bottles - https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01 

  vector<pair<int, int>> testcases = {
    {1,2},{5,10},{2,2},{9,3},{15,4},{8,4},{100,99},{100,2}
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->numWaterBottles(tc.first, tc.second) << endl;
  }
}

class Solution2 {
  bool nextPermutation(vector<int>& arr, int N) {
    int index = N - 2;

    while (index >= 0) {
      if (arr[index] < arr[index + 1]) break;
      index--;
    }

    if (index == -1) return false;

    for (int i = N - 1; i > index; i--) {
      if (arr[i] > arr[index]) {
        swap(arr[index], arr[i]);
        break;
      }
    }

    reverse(arr.begin() + index + 1, arr.end());

    return true;
  }

public:
  vector<vector<int>> uniquePerms(vector<int>& arr) {
    // code here

    int N = arr.size();
    vector<vector<int>> perms;

    sort(arr.begin(), arr.end());

    perms.push_back(arr);

    while (nextPermutation(arr, N)) {
      perms.push_back(arr);
    }

    return perms;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N! * 2N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks All Unique Permutations of an array - https://www.geeksforgeeks.org/problems/all-unique-permutations-of-an-array/1 

  vector<vector<int>> testcases = {
    {1},
    {1,2,3},
    {1,3,3},
    {1,2,2,4},
    {1,2,3,4},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    for (auto& e : tc) cout << e << " ";
    cout << endl;
    vector<vector<int>> perms = s2->uniquePerms(tc);
    for (auto& perm : perms) {
      for (auto& e : perm) cout << e << " ";
      cout << endl;
    }
    cout << endl;
  }
}

int main() {
  // Day 1 of October 2025

  p1();

  p2();

  return 0;
}
