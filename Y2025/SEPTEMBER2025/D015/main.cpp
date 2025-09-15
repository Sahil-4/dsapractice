#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int solve1(string& text, string& brokenLetters) {
    unordered_set<char> brokenLettersSet(brokenLetters.begin(), brokenLetters.end());

    int wordCount = 0; // which can be typed
    bool flag = true;

    for (int i = 0; i < text.size(); i++) {
      if (text[i] == ' ') {
        if (flag) wordCount++;
        flag = true;
      }
      else if (brokenLettersSet.find(text[i]) != brokenLettersSet.end()) {
        flag = false;
      }
    }

    if (flag) wordCount++;

    return wordCount;

    // Complexity analysis
    // Time : O(M) + O(N)
    // Space : O(M)
  }

  void setBit(int& num, int i) {
    int mask = 1;
    mask = mask << i;
    num = num | mask;
  }

  int getBit(int& num, int i) {
    return ((num >> i) & 1);
  }

  int index(char& ch) {
    return (ch - 'a');
  }

  int solve2(string text, string brokenLetters) {
    // initially no bit is set 
    int hash = 0;
    for (char& ch : brokenLetters) setBit(hash, index(ch));

    int wordCount = 0;
    bool flag = true;

    for (char& ch : text) {
      if (ch == ' ') {
        if (flag) wordCount++;
        flag = true;
      }
      else if (getBit(hash, index(ch))) {
        flag = false;
      }
    }

    if (flag) wordCount++;

    return wordCount;

    // Complexity analysis
    // Time : O(M) + O(N)
    // Space : O(1)
  }

public:
  int canBeTypedWords(string text, string brokenLetters) {
    // text = "hello world", brokenLetters = "ad"
    // make a set of brokenLettersSet = { a, d }
    // keep a boolean flag; // initially true
    // traverse text from i = 0, to i < text.length
    // for each char i,
    // if it present in brokenLettersSet,
    // make flag = false
    // else if char i is a space,
    // if flag is true increment wordCount
    // set flag =  true
    // after loop 
    // at the end again 
    // if flag is true increment wordCount 
    // TIP: instead of using set (or map) for broken letters 
    // we can use a 32 bit mask also 
    // and use its bits as index of broken letters 
    // idea behind this is that the number of total letters is 26, 
    // that can be either a broker or a good one 
    // which can be seen as boolean flag 
    // a 32 bit integer can be used to represent this 

    // return solve1(text, brokenLetters);
    return solve2(text, brokenLetters);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1935. Maximum Number of Words You Can Type - https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15

  vector<pair<string, string>> testcases = {
    {"hello world", "ad"},
    {"leet code", "lt"},
    {"leet code", "e"},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    string text = tc.first;
    string brokenLetters = tc.second;
    cout << "INPUT: " << endl;
    cout << "text: " << text << endl;
    cout << "brokenLetters: " << brokenLetters << endl;
    int count = s1->canBeTypedWords(text, brokenLetters);
    cout << "OUTPUT: " << count << endl;
    cout << endl;
  };
}

class Solution2 {
public:
  bool stringStack(string& pattern, string& target) {
    // code here
    // pattern = "geuaek", target = "geek"
    // keep two stacks (or pointers)
    // pi for pattern, ti for target 
    // start from back 
    // if pattern[pi] == target[ti]
    // decrement both by one 
    // else 
    // decrement pi by two 
    // if ti reaches -1 return true 

    int pi = pattern.size() - 1;
    int ti = target.size() - 1;

    while (pi >= 0 && ti >= 0) {
      if (pattern[pi] == target[ti]) {
        pi -= 1;
        ti -= 1;
      }
      else {
        pi -= 2;
      }
    }

    return ti == -1;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks String stack - https://www.geeksforgeeks.org/problems/string-stack--165812/1

  vector<pair<string, string>> testcases = {
    {"geuaek", "geek"},
    {"agiffghd", "gfg"},
    {"ufahs", "aus"},
    {"dicxdcubad", "dia"},
    {"bmmbgfalayg", "mba"},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    string pattern = tc.first;
    string target = tc.second;
    cout << "INPUT: " << endl;
    cout << "pattern: " << pattern << endl;
    cout << "target: " << target << endl;
    bool check = s2->stringStack(pattern, target);
    cout << "OUTPUT: " << check << endl;
    cout << endl;
  };
}

int main() {
  // Day 15 of September 2025

  p1();

  p2();

  return 0;
}
