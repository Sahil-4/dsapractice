#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <unordered_set>

using namespace std;

bool wordBreak_solution1(string s, vector<string>& wordDict) {
    if (s == "") return true;

    for (int it = 0; it < s.length(); it++) {
        string temp = s.substr(0, it + 1);
        if (find(wordDict.begin(), wordDict.end(), temp) != wordDict.end()) {
            s.erase(0, temp.length());
            bool out = wordBreak(s, wordDict);
            if (out) return true;
            s.insert(0, temp);
        }
    }

    return false;

    // TLE 
}

// for memoization 
int memo[301];

bool solve(string s, int idx, unordered_set<string> &dict) {
    if (idx == s.length()) return true;
    if (dict.find(s) != dict.end()) return true;
    if (memo[idx] != -1) return memo[idx];

    for (int len = 1; len <= s.length(); len++) {
        string temp = s.substr(idx, len);

        if (dict.find(temp) != dict.end()) {
            if (dict.find(s) != dict.end()) return memo[idx] = true;
            if (solve(s, idx + temp.length(), dict)) return memo[idx] = true;
        }
    }

    return memo[idx] = false;
}

bool wordBreak(string s, vector<string>& wordDict) {
    memset(memo, -1, sizeof(memo));

    unordered_set<string> dict;
    for (string word : wordDict) dict.insert(word);

    return solve(s, 0, dict);
}

void p1() {
    // Problem 1 : Leetcode 139. Word Break - https://leetcode.com/problems/word-break/ 

    string s = "";
    vector<string> wordDict = {};
    bool check = wordBreak(s, wordDict);
    cout << check << endl;
}


int main() {
    // Day 29 

    p1();


    return 0;
}
