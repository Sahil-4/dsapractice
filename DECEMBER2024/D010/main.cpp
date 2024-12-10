#include <bits/stdc++.h>

using namespace std;

string brute(string s) {
    // make a copy and reverse it 
    string rev = s;
    reverse(rev.begin(), rev.end());

    // find the largest prefix palindrome 
    for (int i = 0; i < s.length(); i++) {
        // MLE - creates new string every time 
        // if (s.substr(0, s.length()-i) == rev.substr(i)) return rev.substr(0, i) + s;
        if (!(memcmp(s.c_str(), rev.c_str() + i, s.length() - i))) return rev.substr(0, i) + s;
    }

    // no prefix is palindrome 
    return rev + s;

    // Complexity analysis 
    // Time : O(N^2) 
    // Space : O(N) 
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

string better(string s) {
    // reverse given string 
    string rev = s;
    reverse(rev.begin(), rev.end());

    // concate both strings 
    string s2 = s + "$" + rev;

    // build lps 
    vector<int> lps = createLPS(s2);

    // find longest palindrome starting from 0 index 
    int lplen = lps.back();

    string out = rev.substr(0, s.length() - lplen) + s;
    return out;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(3N) copy string 
}

string shortestPalindrome(string s) {
    // brute force 
    // return brute(s);

    // using LPS logic 
    return better(s);
}

void p1() {
    // Problem 1 : Leetcode 214. Shortest Palindrome - https://leetcode.com/problems/shortest-palindrome/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/0 

    cout << shortestPalindrome("aba") << endl;
    cout << shortestPalindrome("ab") << endl;
    cout << shortestPalindrome("abc") << endl;
    cout << shortestPalindrome("abcba") << endl;
}

int main() {
    // Day 10 of December 

    p1();


    return 0;
}