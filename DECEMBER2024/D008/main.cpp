#include <bits/stdc++.h>

using namespace std;


const int mod = 10000007;

int rabin_karp(string src, string target) {
    int n = target.length();

    int power = 1;
    for (int i = 0; i < n; i++) {
        power = (power * 29) % mod;
    }

    int targetCode = 0; // for string target
    for (int i = 0; i < n; i++) {
        targetCode = (targetCode * 29 + target[i]) % mod;
    }

    int hashCode = 0; // for string src
    for (int i = 0; i < src.length(); i++) {
        hashCode = (hashCode * 29 + src[i]) % mod;
        if (i < n - 1) continue;

        if (i >= n) hashCode = (hashCode - src[i - n] * power) % mod;

        if (hashCode < 0) hashCode += mod;

        if (hashCode == targetCode) {
            if (src.substr(i - n + 1, n) == target) return i - n + 1;
        }
    }

    return -1;

    // Complexity analysis 
    // Time : O(n+m) 
    // Space : O(1) 
}

int repeatedStringMatch(string a, string b) {
    if (a == b) return 1;

    int cnt = 1;
    string scr = a;
    while (scr.length() < b.length()) {
        cnt++;
        scr += a;
    }

    if (rabin_karp(scr, b) != -1) return cnt;
    if (rabin_karp(scr + a, b) != -1) return cnt + 1;
    return -1;
}

void p1() {
    // Problem 1 : Leetcode 686. Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/repeated-string-match--141631/0 

    cout << repeatedStringMatch("abcs", "abcs") << endl;
}


int main() {
    // Day 8 of December - String Matching & Hashing 

    p1();


    return 0;
}