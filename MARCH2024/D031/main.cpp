#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 0) return "";
    if (strs.size() == 1) return strs[0];

    sort(strs.begin(), strs.end());

    string commonPrefix = "";
    int l = strs.size() - 1;

    for (int i = 0; i < strs[0].length() && i < strs[l].length(); i++) {
        if (strs[0][i] != strs[l][i]) return commonPrefix;
        commonPrefix += strs[0][i];
    }

    return commonPrefix;
}

void p1() {
    // Problem 1 : Leetcode 14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/ 

    // vector<string> arr = {"flower","flow","flight"};
    vector<string> arr = {"abc","bca","cba"};

    string common = longestCommonPrefix(arr);

    cout << "common : " << common << endl;
}

bool isIsomorphic(string s, string t) {
    if (s.length() != t.length()) return false;

    map<char, char> charmap1;
    map<char, char> charmap2;

    for (int i = 0; i < s.length(); i++) {
        if (charmap1.find(s[i]) == charmap1.end() && charmap2.find(t[i]) == charmap2.end()) {
            charmap1.insert({s[i], t[i]});
            charmap2.insert({t[i], s[i]});
        } else {
            if (charmap1[s[i]] != t[i]) return false;
            if (charmap2[t[i]] != s[i]) return false;
        }
    }

    return true;
}

void p2() {
    // Problem 2 : LC 205. Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/ 

    // string s = "egg", t = "add";
    string s = "bbbaaaba", t = "aaabbbba";

    bool iso = isIsomorphic(s, t);
    cout << "iso : " << iso << endl;
}

int main() {
    // Day 31 

    p1();

    p2();


    return 0;
}