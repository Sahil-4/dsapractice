#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  bool knowsLanguage(unordered_set<int>& languagesU, int l) {
    return (languagesU.find(l) != languagesU.end());
  }

  bool hasCommonLanguage(vector<vector<int>>& languages, int u, int v) {
    if (languages[u].size() > languages[u].size()) {
      return hasCommonLanguage(languages, v, u);
    }

    vector<int> languagesU = languages[u];
    unordered_set<int> languagesV(begin(languages[v]), end(languages[v]));

    for (auto& l : languagesU) {
      if (knowsLanguage(languagesV, l)) return true;
    }

    return false;
  }

public:
  int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
    unordered_set<int> usersToTeach;

    for (auto& friendship : friendships) {
      int u = friendship[0] - 1, v = friendship[1] - 1;
      if (!hasCommonLanguage(languages, u, v)) {
        usersToTeach.insert(u);
        usersToTeach.insert(v);
      }
    }

    vector<int> userKnowsLanguage(n + 1, 0);
    int mostknownLanguage = 0;

    for (auto& user : usersToTeach) {
      for (auto& language : languages[user]) {
        userKnowsLanguage[language]++;
        if (userKnowsLanguage[language] > userKnowsLanguage[mostknownLanguage]) {
          mostknownLanguage = language;
        }
      }
    }

    return usersToTeach.size() - userKnowsLanguage[mostknownLanguage];

    // Complexity analysis 
    // Time : O(N * N * Log(N)) + O(N * N) 
    // Space : O(M + 2N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1733. Minimum Number of People to Teach - https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10

  class TEST {
  public:
    int n;
    vector<vector<int>> languages;
    vector<vector<int>> friendships;

    TEST(int n, vector<vector<int>> languages, vector<vector<int>> friendships) {
      this->n = n;
      this->languages = languages;
      this->friendships = friendships;
    }

    void print() {
      cout << "n : " << n;
      cout << endl;

      cout << "languages: ";
      for (int u = 0; u < languages.size(); u++) {
        cout << "[ ";
        for (int li = 0; li < languages[u].size(); li++) {
          cout << languages[u][li] << " ";
        }
        cout << "] ";
      }
      cout << endl;

      cout << "friendships: ";
      for (auto& friendship : friendships) {
        int u = friendship[0], v = friendship[1];
        cout << "[ " << u << " " << v << " ] ";
      }
      cout << endl;
      cout << endl;
    }
  };

  vector<TEST> testcases = {
    TEST(2, {{1},{2},{1,2}}, {{1,2},{1,3},{2,3}}),
    TEST(3, {{2},{1,3},{1,2},{3}}, {{1,4},{1,2},{3,4},{2,3}}),
  };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    cout << "INPUT: " << endl;
    tc.print();
    int out = s1->minimumTeachings(tc.n, tc.languages, tc.friendships);
    cout << "OUTPUT: " << out << endl << endl;
  }
}

class Solution2 {
public:
  string largestSwap(string& s) {
    int N = s.size();

    // precompute max element on right 
    vector<int> rightMaxIndex(N);
    rightMaxIndex[N - 1] = N - 1;
    for (int i = N - 2; i >= 0; i--) {
      if (s[i] > s[rightMaxIndex[i + 1]]) {
        rightMaxIndex[i] = i;
      }
      else {
        rightMaxIndex[i] = rightMaxIndex[i + 1];
      }
    }

    // for i if we can swap with any j 
    // we swap and break 
    for (int i = 0; i < N; i++) {
      int j = rightMaxIndex[i];
      if (s[j] > s[i]) {
        swap(s[i], s[j]);
        break;
      }
    }

    return s;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Largest number in one swap - https://www.geeksforgeeks.org/problems/largest-number-in-one-swap1520/1

  vector<string> testcases = {
    "123",
    "321",
    "12345",
    "54321",
    "74828",
    "3099",
    "9099",
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    cout << "INPUT: " << tc << endl;
    string out = s2->largestSwap(tc);
    cout << "OUTPUT: " << out << endl << endl;
  }
}

int main() {
  // Day 10 of September 2025

  p1();

  p2();

  return 0;
}
