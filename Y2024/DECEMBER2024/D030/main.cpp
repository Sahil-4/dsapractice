#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    string rle(string s) {
        string rle_string = "";

        for (int index = 1, count = 1; index <= s.size(); index++) {
            if (index == s.size() || s[index] != s[index - 1]) {
                rle_string = rle_string + to_string(count) + s[index - 1];
                count = 0;
            }
            count++;
        }

        return rle_string;
    }

    string recursive(int N) {
        if (N == 1) return "1";
        return rle(recursive(N - 1));

        // Complexity analysis 
        // Time : O(N * S_len) 
        // Space : O(N) stack 
    }

    string iterative(int N) {
        string s = "1";

        for (int n = 2; n <= N; n++) {
            string rle_string = "";

            for (int index = 1, count = 1; index <= s.size(); index++) {
                if (index == s.size() || s[index] != s[index - 1]) {
                    rle_string = rle_string + to_string(count) + s[index - 1];
                    count = 0;
                }
                count++;
            }

            s = rle_string;
        }

        return s;

        // Complexity analysis 
        // Time : O(N * s_len) 
        // Space : O(1) 
    }

public:
    string countAndSay(int N) {
        // return recursive(N);

        return iterative(N);
    }
};

void p1() {
    // Problem 1 : Leetcode 38. Count and Say - https://leetcode.com/problems/count-and-say/ 

    cout << Problem1().countAndSay(5) << endl;
    cout << Problem1().countAndSay(12) << endl;
    cout << Problem1().countAndSay(18) << endl;
}

class Problem2 {
    int PRIME = 101;

    long long generateHash(string s) {
        long long hash = 0;

        for (int i = 0; i < s.length(); i++) {
            hash += ((long long)(s[i] - 'a') * pow(PRIME, i));
        }

        return hash;
    }

    long long updateHash(long long& oldhash, char oldc, char newc, int plen) {
        long long newhash = (oldhash - (oldc - 'a')) / PRIME;
        newhash += ((long long)(newc - 'a') * pow(PRIME, plen - 1));
        return newhash;
    }

    int rabin_karp(string& text, string& pattern) {
        // search pattern in text using rabin karp algorithm 

        int tlen = text.length();
        int plen = pattern.length();

        long long patternhash = generateHash(pattern);
        long long texthash = generateHash(text.substr(0, plen));

        for (int i = 0; i <= tlen - plen; i++) {
            if (patternhash == texthash) {
                // might be a hash collision check whether both strings are equal or not 
                if (text.substr(i, plen) == pattern) return i;
            }

            if (i < tlen - plen) {
                // update text hash 
                texthash = updateHash(texthash, text[i], text[i + plen], plen);
            }
        }

        return -1;

        // Complexity analysis 
        // Time : O(plen + tlen * plen) 
        // Space : O(1) + creating temporary substrings 
    }

public:
    int repeatedStringMatch(string a, string b) {
        // Your code goes here 

        // intution 
        // string b will be repetition of a 
        // and then there will be sub sequence of a at the beginning 
        // and/or at the end of b 

        // idea 
        // min reps = len(b) / len(a) 
        // max reps = min reps + 2 
        // out = min_reps, min_reps+1 or min_reps+2 

        int min_reps = 1;
        if (b.length() > a.length()) min_reps = b.length() / a.length();

        string text = "";

        // repeat a min_reps times 
        for (int i = 0; i < min_reps; i++) text = text + a;

        // b is pattern we have to search in text 
        int check = rabin_karp(text, b);
        if (check != -1) return min_reps;

        text = text + a;
        min_reps++;
        check = rabin_karp(text, b);
        if (check != -1) return min_reps;

        text = text + a;
        min_reps++;
        check = rabin_karp(text, b);
        if (check != -1) return min_reps;

        return -1;

        // we are manipulating string a and concatenating it some K times 
        // so k * len(a) will be added to time compelxity 
    }
};

void p2() {
    // Problem 2 : Geeksforgeeks Repeated String Match (Rebin karp) - https://www.geeksforgeeks.org/problems/repeated-string-match--141631/0 

    cout << Problem2().repeatedStringMatch("abc", "abc") << endl;
    cout << Problem2().repeatedStringMatch("abc", "abcabcabc") << endl;
    cout << Problem2().repeatedStringMatch("abc", "abcabcabcab") << endl;
    cout << Problem2().repeatedStringMatch("abc", "cabcabcabcab") << endl;
    cout << Problem2().repeatedStringMatch("abc", "bcabcabcabcab") << endl;
}


int main() {
    // Day 30 of December 2024 

    p1();

    p2();


    return 0;
}