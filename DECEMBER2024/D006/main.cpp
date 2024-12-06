#include <bits/stdc++.h>

using namespace std;

int brute(string& haystack, string& needle) {
    // both strings are same 
    if (needle == haystack) return 0;

    // needle is larger string 
    if (needle.length() >= haystack.length()) return -1;

    for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        int j = 0;

        while (j < needle.length() && haystack[i + j] == needle[j]) j++;

        if (j == needle.length()) return i;
    }

    return -1;

    // Complexity analysis 
    // Time : O(N * M) in worst case 
    // Space : O(1) 
}

vector<int> createLPS(string& pattern) {
    int m = pattern.size();
    vector<int> lps(m, 0);

    for (int llen = 0, i = 1; i < m;) {
        if (pattern[i] == pattern[llen]) {
            lps[i] = llen + 1;
            llen++, i++;
        } else {
            if (llen != 0) llen = lps[llen - 1];
            else lps[i] = 0, i++;
        }
    }

    return lps;

    // Complexity analysis 
    // Time : O(m) 
    // Space : O(1) 
}

int kmp(string& text, string& pattern) {
    // Kruth Morris Pratt 

    // prepare lps 
    vector<int> lps = createLPS(pattern);

    // --------- perform kmp --------- 

    vector<int> occurrs;

    int N = text.length(), M = pattern.length();

    int i = 0, j = 0;
    bool flag = false;

    while (i < N) {
        if (text[i] == pattern[j]) {
            i++, j++;
        } else {
            if (j != 0) j = lps[j - 1];
            else i++;
        }

        if (j == M) {
            occurrs.push_back(i - M);
            j = lps[j - 1];
            flag = true;
        }
    }

    return occurrs.size() == 0 ? -1 : occurrs[0];

    // Complexity analysis 
    // Time : O(N + M) 
    // Space : O(M) + start index of all occurrences 
}

int strStr(string haystack, string needle) {
    // brute force 
    // return brute(haystack, needle);

    return kmp(haystack, needle);
}

void p1() {
    // Problem 1 : Leetcode 28. Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/1 

    cout << strStr("sadbutsad", "sad") << endl;
    cout << strStr("leetcode", "leeto") << endl;
}

int main() {
    // Day 6 of December - String Hard 

    p1();


    return 0;
}
