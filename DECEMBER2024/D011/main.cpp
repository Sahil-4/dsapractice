#include <bits/stdc++.h>

using namespace std;

void buildLPS(vector<int>& lps, string& str, int N) {
    // brute way - O(N^2) 
    // for (int i = 1; i < N; i++) {
    //     int j = 0, k = i;
    //     while (k < N && str[j] == str[k]) j++, k++;
    //     lps[i] = j;
    // }

    // better way - O(N) 
    for (int llen = 0, i = 1; i < N;) {
        if (str[i] == str[llen]) {
            lps[i] = llen + 1;
            llen++, i++;
        }
        else {
            if (llen != 0) llen = lps[llen - 1];
            else lps[i] = 0, i++;
        }
    }
}

string sol1(string& s) {
    // Approach 
    // trying kmp lps 
    // we will find the lps and then we will take the last lps 
    // for prefix and suffix both 
    // we will return substring from 0, with len of last lps 

    int N = s.length();

    vector<int> lps(N, 0);
    buildLPS(lps, s, N);

    return s.substr(0, lps.back());

    // Complexity analysis 
    // Time : O(N) + O(N) 
    // Space : O(N) 
}

string longestPrefix(string s) {
    return sol1(s);
}

void p1() {
    // Problem 1 : Leetcode 1392. Longest Happy Prefix - https://leetcode.com/problems/longest-happy-prefix/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1 

    cout << longestPrefix("a") << endl;
    cout << longestPrefix("ab") << endl;
    cout << longestPrefix("abc") << endl;
    cout << longestPrefix("aba") << endl;
    cout << longestPrefix("abab") << endl;
    cout << longestPrefix("ababc") << endl;
}


int main() {
    // Day 11 of December 

    p1();


    return 0;
}