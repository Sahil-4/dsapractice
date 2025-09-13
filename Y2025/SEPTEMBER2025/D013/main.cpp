#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxFreqSum(string s) {
    vector<int> frequency(26, 0);
    for (auto& ch : s) {
      frequency[ch - 'a']++;
    }

    int vowelMaxFrequency = 0;
    int consoMaxFrequency = 0;

    for (int i = 0; i < 26; i++) {
      if (i == 0 || i == 4 || i == 8 || i == 14 || i == 20) {
        vowelMaxFrequency = max(vowelMaxFrequency, frequency[i]);
      }
      else {
        consoMaxFrequency = max(consoMaxFrequency, frequency[i]);
      }
    }

    return vowelMaxFrequency + consoMaxFrequency;

    // Complexity analysis
    // Time : O(N) + O(26)
    // Space : O(26)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3541. Find Most Frequent Vowel and Consonant - https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13

  vector<string> testcases = { "successes", "aeiaeia", "nnnxxxx" };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << "INPUT: " << tc << endl;
    cout << "OUTPUT: " << s1->maxFreqSum(tc) << endl;
    cout << endl;
  }
}

class Solution2 {
public:
  int minCost(int n, int m, vector<int>& x, vector<int>& y) {
    //  code here

    // !MODIFYING INPUT 
    sort(x.begin(), x.end(), greater<int>());
    sort(y.begin(), y.end(), greater<int>());

    int H = 1; // horizontal segments 
    int i = 0; // pointer for x 
    int V = 1; // vertical segments 
    int j = 0; // pointer for y 

    int totalCost = 0;

    while (i < x.size() || j < y.size()) {
      if (i >= x.size()) {
        totalCost += (y[j] * V);
        H++;
        j++;
      }
      else if (j >= y.size()) {
        totalCost += (x[i] * H);
        V++;
        i++;
      }
      else if (x[i] >= y[j]) {
        totalCost += (x[i] * H);
        V++;
        i++;
      }
      else {
        totalCost += (y[j] * V);
        H++;
        j++;
      }
    }

    return totalCost;

    // Complexity analysis 
    // Time : O(2 * N * Log(N)) + O(2N) 
    // Space : (1) + modifying input array 
  }
};


void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimum Cost to cut a board into squares - https://www.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1

  class TESTCASE {
  public:
    int n;
    int m;
    vector<int> x;
    vector<int> y;

    TESTCASE(int n, int m, vector<int> x, vector<int> y) {
      this->n = n;
      this->m = m;
      this->x = x;
      this->y = y;
    }

    void print() {
      cout << "n: " << n << endl;
      cout << "m: " << m << endl;
      cout << "x: ";
      for (auto& e : x) cout << e << " ";
      cout << endl;
      cout << "y: ";
      for (auto& e : y) cout << e << " ";
      cout << endl;
    }
  };
  vector<TESTCASE> testcases = {
    TESTCASE(4, 6, {2, 1, 3, 1, 4}, {4, 1, 2}),
    TESTCASE(4, 4, {1, 1, 1}, {1, 1, 1}),
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT: " << endl;
    tc.print();
    cout << "OUTPUT: " << s2->minCost(tc.n, tc.m, tc.x, tc.y) << endl;
      cout << endl;
  }
}

int main() {
  // Day 13 of September 2025

  p1();

  p2();

  return 0;
}
