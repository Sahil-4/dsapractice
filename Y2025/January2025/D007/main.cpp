#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    string convert(string s, int nr) {
        if (nr <= 1) return s;

        vector<string> v(nr, "");

        int ri = 0; // start from 0, move to nr-1, then come back to 0 
        bool forward = true;

        for (char c : s) {
            v[ri] += c;
            if (ri == nr - 1 && forward) {
                ri--;
                forward = false;
            }
            else if (ri == 0 && !forward) {
                ri++;
                forward = true;
            }
            else if (forward) {
                ri++;
            }
            else {
                ri--;
            }
        }

        // join all nr strings 
        string out = "";
        for (string s : v) out += s;
        return out;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(N) 
    }
};

void p1() {
    // Problem 1 : Leetcode 6. Zigzag Conversion - https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/concatenation-of-zig-zag-string-in-n-rows0308/1 
    // My solution posted : 
    // https://leetcode.com/problems/zigzag-conversion/solutions/6243167/simple-and-easy-to-understand-with-diagr-mypa

    cout << Problem1().convert("PAYPALISHIRING", 1) << endl;
    cout << Problem1().convert("PAYPALISHIRING", 2) << endl;
    cout << Problem1().convert("PAYPALISHIRING", 3) << endl;
    cout << Problem1().convert("PAYPALISHIRING", 17) << endl;
}

class Problem2 {
    int brute(string& haystack, string& needle) {
        // n^2 string traversal and comparisons 

        int n = haystack.length(), m = needle.length();

        for (int i = 0; i <= n - m; i++) {
            if (haystack[i] != needle[0]) continue;
            for (int j = 0; j < m; j++) {
                if (haystack[i + j] != needle[j]) break;
                if (j == m - 1) return i;
            }
        }

        return -1;

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(1) 
    }

    vector<int> buildLCPS(string& text, int N) {
        vector<int> lcps(N, 0);

        for (int i = 1, llpslen = 0; i < N; i++) {
            while (llpslen > 0 && text[i] != text[llpslen]) llpslen = lcps[llpslen - 1];
            if (text[i] == text[llpslen]) lcps[i] = ++llpslen;
        }

        return lcps;
    }

    int kmp(string& haystack, string& needle) {
        int n = haystack.length(), m = needle.length();
        if (m > n) return -1;

        vector<int> lcps = buildLCPS(needle, m);

        // pointers to iterate over strings 
        int i = 0, j = 0;
        while (i < n) {
            if (haystack[i] == needle[j]) {
                i++, j++;
            }
            else {
                if (j != 0) j = lcps[j - 1];
                else i++;
            }

            // if we reached end after searching 
            if (j == m) return i - m;
        }

        return -1;

        // Complexity analysis 
        // Time : O(N+M) build lcsp + char match 
        // Space : O(N) longest common suf & pref 
    }

public:
    int strStr(string haystack, string needle) {
        // return brute(haystack, needle);

        return kmp(haystack, needle);
    }
};

void p2() {
    // Problem 2 : Leetcode 28. Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/0 

    cout << Problem2().strStr("abcdefghi", "xyz") << endl;
    cout << Problem2().strStr("abcdefghi", "abc") << endl;
    cout << Problem2().strStr("abcdefghi", "ghi") << endl;
    cout << Problem2().strStr("abcdefghi", "cde") << endl;
    cout << Problem2().strStr("abcdefghi", "cdeh") << endl;
}


int main() {
    // Day 7 of January 2025 

    p1();

    p2();


    return 0;
}