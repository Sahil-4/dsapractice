#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  bool doesAliceWin(string s) {
    auto check = [](char ch) {
      return string("aeiou").find(ch) != string::npos;
      };
    return any_of(s.begin(), s.end(), check);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3227. Vowels Game in a String - https://leetcode.com/problems/vowels-game-in-a-string/description/?envType=daily-question&envId=2025-09-12

  vector<string> testcases = { "leetcoder", "leetcode", "bbcd" };
  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << "INPUT: " << tc << endl;
    cout << "OUTPUT: " << s1->doesAliceWin(tc) << endl;
    cout << endl;
  }
}

class Solution2 {
private:
  int getDiffWithP(vector<int>& arr, int N, int k, int p) {
    int newMin = min(arr[0] + k, arr[p + 1] - k);
    int newMax = max(arr[N - 1] - k, arr[p] + k);
    if (arr[p + 1] - k < 0) return INT_MAX;
    return newMax - newMin;
  }

public:
  int getMinDiff(vector<int>& arr, int k) {
    // code here
    // k = 2, arr[] = [1, 5, 8, 10]
    // inc[] = [3, 7, 10, 12]
    // dec[] = [8, 6, 3, -1]
    // out = 5
    // sort the given array 
    // increment half of array elements and decrement other half 
    // find min and max 
    // return difference 

    int N = arr.size();

    if (N == 1) return 0;

    // MODIFYING INPUT 
    sort(arr.begin(), arr.end());

    int minDiff = arr[N - 1] - arr[0];

    for (int p = 0; p < N - 1; p++) {
      int diff = getDiffWithP(arr, N, k, p);
      minDiff = min(minDiff, diff);
    }

    return minDiff;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N) 
    // Space : O(1) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimize the Heights II - https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1

  vector<pair<int, vector<int>>> testcases = {
    {2, {1, 5, 8, 10}},
    {3, {3, 9, 12, 16, 20}},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    auto k = tc.first;
    auto arr = tc.second;
    cout << "INPUT: ";
    cout << endl;
    cout << "k: " << k;
    cout << endl;
    cout << "arr: ";
    for (auto& e : arr) cout << e << " ";
    cout << endl;
    int out = s2->getMinDiff(arr, k);
    cout << "OUTPUT: " << out << endl;
    cout << endl;
  }
}

int main() {
  // Day 12 of September 2025

  p1();

  p2();

  return 0;
}
