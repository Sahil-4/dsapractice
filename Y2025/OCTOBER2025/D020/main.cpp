#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int finalValueAfterOperations(vector<string>& operations) {
    int X = 0;

    for (const string& operation : operations) {
      if (operation == "++X" || operation == "X++") {
        X += 1;
      } else {
        X -= 1;
      }
    }

    return X;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2011. Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-20 

  vector<vector<string>> testcases = {
    {"--X","X++","X++"},
    {"++X","++X","X++"},
    {"X++","++X","--X","X--"},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->finalValueAfterOperations(tc) << endl;
  }
}

class Solution2 {
private:
  vector<int> generateCatalan(int N) {
    vector<int> catalan(N + 1, 0);
    catalan[0] = 1;

    for (int i = 1; i < N + 1; i++) {
      for (int j = 0; j < i; j++) {
        catalan[i] += (catalan[j] * catalan[i - 1 - j]);
      }
    }

    return catalan;
  }

public:
  vector<int> countBSTs(vector<int>& arr) {
    // Code here
    // arr[] = [ 1,2,3,4 ]
    int N = arr.size();

    vector<int> copy(arr);
    sort(copy.begin(), copy.end());

    vector<int> catalan = generateCatalan(N);

    vector<int> output(N);

    for (int i = 0; i < N; i++) {
      auto it = lower_bound(copy.begin(), copy.end(), arr[i]);
      int index = it - copy.begin();

      int left = index;
      int right = N - index - 1;

      output[i] = catalan[left] * catalan[right];
    }

    return output;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Number of BST From Array - https://www.geeksforgeeks.org/problems/number-of-bst-from-array/1 

  vector<vector<int>> testcases = {
    { 1, 2 },
    { 1, 2, 2 },
    { 1, 2, 3 },
    { 1, 2, 3, 4, 5 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> output = s2->countBSTs(tc);
    for (auto& e : output) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 20 of October 2025

  p1();

  p2();

  return 0;
}
