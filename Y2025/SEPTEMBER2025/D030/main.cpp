#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int solve1(vector<int>& nums) {
    // simulate the process step by step
    // at any point, 
    // we only need two arrays: 
    // the current row and the next row

    int N = nums.size();
    vector<int> curr(nums.begin(), nums.end());

    for (int x = N - 1; x > 0; x--) {
      vector<int> next(x, 0);
      for (int i = 0; i < x; i++) {
        next[i] = (curr[i] + curr[i + 1]) % 10;
      }
      curr = next;
    }

    return curr[0];

    // complexity analysis:
    // time  : o(N^2)
    // space : o(N)
  }

  int solve2(vector<int>& nums) {
    // optimized simulation using a single array
    // update in-place: new[i] = old[i] + old[i+1]
    // next[i] = (curr[i] + curr[i + 1]) % 10; will become
    // curr[i] = (curr[i] + curr[i + 1]) % 10;

    int N = nums.size();
    vector<int> dummy(nums.begin(), nums.end());

    for (int x = N - 1; x > 0; x--) {
      for (int i = 0; i < x; i++) {
        dummy[i] = (dummy[i] + dummy[i + 1]) % 10;
      }
    }

    return dummy[0];

    // complexity analysis:
    // time  : o(N^2)
    // space : o(N)
  }

public:
  int triangularSum(vector<int>& nums) {
    // return solve1(nums);
    return solve2(nums);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2221. Find Triangular Sum of an Array - https://leetcode.com/problems/find-triangular-sum-of-an-array/description/?envType=daily-question&envId=2025-09-30 

  vector<vector<int>> testcases = {
    { 1,2,3,4,5 },
    { 5 },
    { 0,7,5,9,6,6,2,2,4,9,1,4,6,2,1,7,4,8,4,6,6,1,6,7,4,0,5,6,4,1 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->triangularSum(tc) << endl;
  }
}

class Solution2 {
private:
  string getBinary(int num, int length) {
    string bin = "";

    while (num != 0) {
      int b = num & 1;
      num = num >> 1;
      bin.push_back('0' + b);
    }

    while (bin.size() < length) bin.push_back('0');

    reverse(bin.begin(), bin.end());

    return bin;
  }

public:
  vector<string> binstr(int N) {
    // code here
    // N = 2
    // 0 -> 2^N
    // 0 -> "00"
    // 1 -> "01"
    // 2 -> "10"
    // 3 -> "11"
    // N = 3
    // 0 -> 2^N
    // 0 -> "000"
    // 1 -> "001"
    // 2 -> "010"
    // 3 -> "011"
    // 4 -> "100"
    // 5 -> "101"
    // 6 -> "110"
    // 7 -> "111"
    // simply run a loop from i = 0 to i < 2^N
    // convert i to binary (or length N, prepending zeroes if needed)
    // and push it to bins 
    // finally return bins 

    vector<string> bins;

    int L = pow(2, N);

    for (int i = 0; i < L; i++) {
      bins.push_back(getBinary(i, N));
    }

    return bins;

    // Complexity analysis 
    // Time : O(L * N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Generate all binary strings - https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1 

  vector<int> testcases = { 1, 2, 3, 5, 10, 15, 20 };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    if (tc > 5) continue;
    vector<string> bins = s2->binstr(tc);
    for (auto& bin : bins) cout << bin << endl;
  }
}

int main() {
  // Day 30 of September 2025

  p1();

  p2();

  return 0;
}
