#include <bits/stdc++.h>

using namespace std;

class Spellchecker {
private:
  unordered_set<string> wordsSet;
  unordered_map<string, string> icaseMap;
  unordered_map<string, string> vnormMap;

  string vowels = "aeiou";

public:
  Spellchecker() {}

  void addWord(string word) {
    string caseNormalisedWord = "";
    string vowelNormalisedWord = "";

    for (auto ch : word) {
      char lch = ch;
      if (lch >= 'A' && lch <= 'Z') {
        lch = 'a' + (lch - 'A');
      }

      char vch = lch;
      if (vowels.find(lch) != string::npos) {
        vch = '.';
      }

      caseNormalisedWord.push_back(lch);
      vowelNormalisedWord.push_back(vch);
    }

    wordsSet.insert(word);

    if (icaseMap.find(caseNormalisedWord) == icaseMap.end()) {
      icaseMap.insert({ caseNormalisedWord, word });
    }
    if (vnormMap.find(vowelNormalisedWord) == vnormMap.end()) {
      vnormMap.insert({ vowelNormalisedWord, word });
    }
  }

  string searchWord(string word) {
    if (wordsSet.find(word) != wordsSet.end()) {
      return word;
    }

    string caseNormalisedWord;
    string vowelNormalisedWord;

    for (auto ch : word) {
      char lch = ch;
      if (lch >= 'A' && lch <= 'Z') {
        lch = 'a' + (lch - 'A');
      }

      char vch = lch;
      if (vowels.find(lch) != string::npos) {
        vch = '.';
      }

      caseNormalisedWord.push_back(lch);
      vowelNormalisedWord.push_back(vch);
    }

    auto it1 = icaseMap.find(caseNormalisedWord);
    if (it1 != icaseMap.end()) return it1->second;

    auto it2 = vnormMap.find(vowelNormalisedWord);
    if (it2 != vnormMap.end()) return it2->second;

    return "";
  }
};

class Solution1 {
public:
  vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
    Spellchecker* sc = new Spellchecker();

    for (auto& word : wordlist) {
      sc->addWord(word);
    }

    vector<string> answer;
    for (auto& word : queries) {
      answer.push_back(sc->searchWord(word));
    }

    return answer;

    // Complexity analysis 
    // Time : O(N * Wi) + O(N * Wi) 
    // Space : O(N + 2N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 966. Vowel Spellchecker - https://leetcode.com/problems/vowel-spellchecker/description/?envType=daily-question&envId=2025-09-14

  vector<pair<vector<string>, vector<string>>> testcases = {
    {
      {"KiTe","kite","hare","Hare"},
      {"kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"},
    },
    {
      { "yellow" },
      { "YellOw" },
    }
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    auto wordlist = tc.first;
    auto queries = tc.second;
    cout << "INPUT: ";
    cout << endl;
    cout << "wordlist: ";
    for (auto w : wordlist) cout << w << " ";
    cout << endl;
    cout << "queries: ";
    for (auto w : queries) cout << w << " ";
    cout << endl;
    auto answer = s1->spellchecker(wordlist, queries);
    cout << "OUTPUT: ";
    for (auto ans : answer) cout << ans << " ";
    cout << endl;
    cout << endl;
  }
}

class Solution2 {
private:
  int sum(vector<int>& arr) {
    return accumulate(arr.begin(), arr.end(), 0);
  }

  int brute(vector<int>& gas, vector<int>& cost) {
    int N = gas.size();

    for (int point = 0; point < N; point++) {
      bool flag = true;
      int fuel = 0;

      for (int i = 0; i < N; i++) {
        // station index - as per circular path 
        int index = (i + point) % N;

        // pick gas from this station 
        fuel += gas[index];
        // try to move to next station 
        fuel -= cost[index];

        // if out of gas while going to next station 
        if (fuel < 0) {
          flag = false;
          break;
        }
      }

      if (flag) return point;
    }

    return -1;

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(1) 
  }

public:
  int startStation(vector<int>& gas, vector<int>& cost) {
    // code here
    // points[] = [0, 1, 2, 3]
    // cost[]   = [6, 6, 3, 5]
    // gas[]    = [4, 5, 7, 4]
    // index 2 is starting point 
    // points[] = [0, 1]
    // cost[]   = [7, 6]
    // gas[]    = [3, 9]
    // not possible return -1
    // points[] = [0, 1]
    // gas[]    = [3, 9]
    // cost[]   = [9, 3]
    // return 1;
    // points[] = [0, 1, 2]
    // gas[]    = [3, 9, 7]
    // cost[]   = [9, 7, 3]
    // return 1;
    // if answer possible, sum(gas) >= sum(cost) holds true 
    // points[] = [0, 1, 2, 3]
    // gas[]    = [3, 7, 3, 9]
    // cost[]   = [7, 9, 3, 3]
    // return 1;
    // say we started from index i, 
    // at any index i + x, if we ran out of fuel, 
    // then we can never reach to index i + x if we start from any index > i and index <= i + x
    // by this we can make a linear solution 

    int N = gas.size();

    if (sum(gas) < sum(cost)) return -1;

    int start = 0; // starting point 
    int fuel = 0; // fuel currently have 

    for (int index = 0; index < N; index++) {
      // pick gas from this station 
      fuel += gas[index];
      // try to move to next station 
      fuel -= cost[index];

      // if out of gas 
      if (fuel < 0) {
        start = index + 1;
        fuel = 0;
      }
    }

    return start;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Gas Station - https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1

  vector<pair<vector<int>, vector<int>>> testcases = {
    { {4, 5, 7, 4}, { 6, 6, 3, 5 } },
    { {3, 9}, { 7, 6 } },
    { {3, 9}, { 9, 3 } },
    { {3, 9, 7}, { 9, 7, 3 } },
    { {3, 7, 3, 9}, { 7, 9, 3, 3} },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> gas = tc.first;
    vector<int> cost = tc.second;
    cout << "INPUT: " << endl;
    cout << "gas: ";
    for (auto& e : gas) cout << e << " ";
    cout << endl;
    cout << "cost: ";
    for (auto& e : cost) cout << e << " ";
    cout << endl;
    cout << "OUTPUT: " << s2->startStation(gas, cost) << endl;
    cout << endl;
  }
}

int main() {
  // Day 14 of September 2025

  p1();

  p2();

  return 0;
}
