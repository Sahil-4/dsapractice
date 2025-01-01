#include <bits/stdc++.h>

using namespace std;


vector<int> preparelps(string& s) {
    int n = s.size();

    // longest common prefix suffix 
    vector<int> lcps(n, 0);

    for (int i = 1, llpslen = 0; i < n; i++) {
        // llpslen = longest lps length till ith index 
        while (llpslen > 0 && s[i] != s[llpslen]) llpslen = lcps[llpslen - 1];
        if (s[i] == s[llpslen]) lcps[i] = ++llpslen;
    }

    return lcps;
}

int kmp(string& text, string& pattern) {
    if (pattern.size() > text.size()) return -1;

    // longest prefix at index i that is also a suffix 
    vector<int> lcps = preparelps(pattern);

    for (int l : lcps) cout << l << " ";
    cout << endl;

    int i = 0, n = text.size();
    int j = 0, m = pattern.size();
    while (i < n) {
        if (text[i] == pattern[j]) {
            i++, j++;
        } else {
            if (j != 0) j = lcps[j - 1];
            else i++;
        }

        if (j == m) return i - j;
    }

    return -1;
}

int strStr(string haystack, string needle) {
    return kmp(haystack, needle);
}

void p1() {
    // Problem 1 : Leetcode 28. Find the Index of the First Occurrence in a String (KMP) - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/search-pattern0205/1 

    cout << strStr("abcabcdabc", "abcd") << endl;
    cout << strStr("abcabcabcabcdabcqrs", "abcd") << endl;
}

int longestPrefixSuffix(string s) {
    // Your code goes here

    vector<int> lcps = preparelps(s);
    return lcps[s.length() - 1];
}

void p2() {
    // Problem 2 : Geeksforgeeks Longest Prefix Suffix - https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1 

    cout << longestPrefixSuffix("abcdaabcabcabcda") << endl;
}


int main() {
    // Day 31 of December 
    // Last day of 2024 

    p1();

    p2();


    return 0;
}
