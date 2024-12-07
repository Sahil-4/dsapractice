#include <bits/stdc++.h>

using namespace std;


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

int repeatedStringMatch(string a, string b) {
    int len_a = a.length(), len_b = b.length();

    int n = len_b / len_a;

    string temp = "";
    int c = n;
    while (c--) temp = temp + a;

    for (int i = 0; i <= 3; i++) {
        if (kmp(temp, b) != -1) return n + i;
        temp = temp + a;
    }

    return -1;

    // Complexity analysis 
    // Time : O(n) + O(3 * (len_temp + len_b)) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 686. Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/repeated-string-match--141631/0 

    cout << repeatedStringMatch("abcd", "cdabcdab") << endl;
    cout << repeatedStringMatch("abcd", "abcda") << endl;
    cout << repeatedStringMatch("abcd", "abcdd") << endl;
}


int main() {
    // Day 7 of December - String hard 

    p1();


    return 0;
}