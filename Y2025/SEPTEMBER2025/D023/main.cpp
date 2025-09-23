#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  vector<string> split(const string& s, char delimiter = ' ') {
    vector<string> tokens;
    string token;
    stringstream ss(s);

    while (getline(ss, token, delimiter)) {
      tokens.push_back(token);
    }

    return tokens;
  }

public:
  int compareVersion(string version1, string version2) {
    // version1 = "1.2", version2 = "1.10"
    // version1[] = [1, 2], version2[] = [1, 10]
    // version1 = "1.01", version2 = "1.001"
    // version1[] = [1, 1], version2[] = [1, 1]
    // version1 = "1.0", version2 = "1.0.0.0"
    // version1[] = [1, 0, 0, 0], version2[] = [1, 0, 0, 0]

    vector<string> tokens1 = split(version1, '.');
    vector<string> tokens2 = split(version2, '.');

    int p1 = 0;
    int p2 = 0;

    while (p1 < tokens1.size() && p2 < tokens2.size()) {
      int vt1 = stoi(tokens1[p1++]), vt2 = stoi(tokens2[p2++]);
      if (vt1 != vt2) return (vt1 < vt2) ? -1 : 1;
    }

    while (p1 < tokens1.size()) {
      int vt1 = stoi(tokens1[p1++]), vt2 = 0;
      if (vt1 != vt2) return (vt1 < vt2) ? -1 : 1;
    }

    while (p2 < tokens2.size()) {
      int vt1 = 0, vt2 = stoi(tokens2[p2++]);
      if (vt1 != vt2) return (vt1 < vt2) ? -1 : 1;
    }

    return 0;

    // Complexity analysis 
    // Time : O(N + M) 
    // Space : O(N + M) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 165. Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23 

  vector<vector<string>> testcases = {
    { "1.2", "1.10" },
    { "1.01", "1.001" },
    { "1.0", "1.0.0.0" },
    { "1", "1.1.0.1.0" },
    { "0", "101.1.100.0.01101.010.1.010.0.0.0.0.0.1.010.0.101.1.1.0.1.1.0.0.1.0.1.0.0.0.1010110011" },
    { "0.0.0.1.0.0.0.0.010.101.0.1.0.1.1.0.0.000.0.1.0.1", "1" },
    { "1.011.0.1.110.01111.0.0.1.0.1.1.1.1.000.0.1.0.0.0", "1.111.1.1" },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->compareVersion(tc[0], tc[1]) << endl;
  }
}

class Solution2 {
public:
  void reverseQueue(queue<int>& q) {
    // code here
    // q[] = [5, 10, 15, 20, 25]
    // stk[] = [5, 10, 15, 20, 25]
    // q[] = [25, 20, 15, 10, 5]

    stack<int> stk;
    while (!q.empty()) {
      stk.push(q.front());
      q.pop();
    }

    while (!stk.empty()) {
      q.push(stk.top());
      stk.pop();
    }

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Queue Reversal - https://www.geeksforgeeks.org/problems/queue-reversal/1 

  vector<queue<int>> testcases = {
    queue<int>({ 5, 10, 15, 20, 25 }),
    queue<int>({ 1, 2, 3, 4, 5 }),
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    s2->reverseQueue(tc);
    while (!tc.empty()) {
      cout << tc.front() << " ";
      tc.pop();
    } cout << endl;
  }
}

int main() {
  // Day 23 of September 2025

  p1();

  p2();

  return 0;
}
