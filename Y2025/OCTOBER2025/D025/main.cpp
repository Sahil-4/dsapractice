#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int totalMoney(int n) {
    // n = 10
    // m -> 1
    // t -> 2
    // w -> 3
    // t -> 4
    // f -> 5
    // s -> 6
    // s -> 7
    // m -> 2
    // t -> 3
    // w -> 4
    // if n = 10, how many sundays will be there ?

    int money = 0;
    int weeks = n / 7;
    for (int i = 1; i <= weeks; i++) {
      // money += sumOf7Terms(i, 1);
      money += ((7 * ((2 * i) + (6))) / 2);
    }

    int left = (n % 7);
    money += ((left * ((2 * (weeks + 1)) + (left - 1))) / 2);

    return money;

    // Complexity analysis 
    // Time : O(weeks) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1716. Calculate Money in Leetcode Bank - https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25 

  vector<int> testcases = {
    1,
    2,
    5,
    7,
    8,
    12,
    15,
    14,
    28,
    32,
    100,
    101,
    107,
    1000,
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->totalMoney(tc) << endl;
  } cout << endl;
}

class Solution2 {
public:
  int minOperations(vector<int>& arr) {
    // code here
    // arr[] = [8, 6, 2]
    // arr[] = [8, 6, 2] (priority queue)
    // osum  = 16
    // tsum = <= 8
    // arr[] = [4, 6, 2] sum = 12 <= 8 false
    // arr[] = [4, 3, 2] sum = 9 <= 8 false
    // arr[] = [4, 3, 1] sum = 8 <= 8 true
    // topr = 3
    // output = 3

    priority_queue<double> pq;
    for (int e : arr) pq.push((double)e);

    double osum = accumulate(arr.begin(), arr.end(), 0.0);
    double tsum = osum / 2.0;
    double csum = osum;

    int topr = 0;

    while (csum > tsum) {
      topr++;

      double top = pq.top(); pq.pop();
      double htop = top / 2.0;

      csum -= top;
      csum += htop;

      pq.push(htop);
    }

    return topr;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimum Steps to Halve Sum - https://www.geeksforgeeks.org/problems/minimum-steps-to-halve-sum/1 

  vector<vector<int>> testcases = {
    { 1, 2, 4, 5, 6, 3, 2, 1, 5, 4, 7, 8, 9, 5, 4, 12 },
    { 8, 6, 2 },
    { 9, 1, 2 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << s2->minOperations(tc) << endl;
  } cout << endl;
}

int main() {
  // Day 25 of October 2025

  p1();

  p2();

  return 0;
}
