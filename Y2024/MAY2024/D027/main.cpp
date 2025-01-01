#include <iostream>

using namespace std;

int characterReplacement_Solution1(string s, int k) {
    int n = s.length();

    if (k == n) return n;

    int longestLen = 0;

    for (int i = 0; i < n; i++) {
        char ch = s[i];
        int len = 1;
        int changesCount = 0;

        // forward case 
        for (int j = i + 1; j < n; j++) {
            if (s[j] != ch && changesCount >= k) break;
            if (s[j] != ch) changesCount++;
            len++;
        }

        // backward case 
        for (int j = i - 1; j >= 0; j--) {
            if (s[j] != ch && changesCount >= k) break;
            if (s[j] != ch) changesCount++;
            len++;
        }

        if (len > longestLen) longestLen = len;
    }

    return longestLen;

    // !TLE - on GFG 
    // Time : O(n ^ 2) 
    // Space : O(1) 
}

int characterReplacement(string s, int k) {
    if (k == s.length()) return k;

    int longestStringLength = 0;
    int maxFreq = 0;
    int charHash[26] = {0};
    int l = 0;

    for (int r = 0; r < s.length(); r++) {
        // update char frequency 
        charHash[s[r] - 'A']++;

        // update freq of char (max freq)
        maxFreq = max(maxFreq, charHash[s[r] - 'A']);

        // remove extra chars if unable to replace them 
        while (r - l + 1 - maxFreq > k) {
            charHash[s[l] - 'A']--;
            maxFreq = 0;
            for (int i = 0; i < 26; i++) maxFreq = max(maxFreq, charHash[i]);
            l++;
        }

        // update max len 
        if (r - l + 1 - maxFreq <= k) longestStringLength = max(longestStringLength, r - l + 1);
    }

    return longestStringLength;

    // Complexity 
    // Time : O((n + n) * 26) 
    // Space : O(26) 
}

int characterReplacement(string s, int k) {
    if (k == s.length()) return k;

    int longestStringLength = 0;

    int charHash[26] = {0};
    int maxFreq = 0;
    int l = 0;

    for (int r = 0; r < s.length(); r++) {
        // update char frequency 
        charHash[s[r] - 'A']++;

        // update freq of char (max freq)
        maxFreq = max(maxFreq, charHash[s[r] - 'A']);

        // remove extra chars if unable to replace them 
        if (r - l + 1 - maxFreq > k) {
            charHash[s[l] - 'A']--;
            l++;
        }

        // update max len 
        if (r - l + 1 - maxFreq <= k) longestStringLength = max(longestStringLength, r - l + 1);
    }

    return longestStringLength;

    // Time : O(n) 
    // Space : O(26) 
}

void p1() {
    // Problem 1 : Leetcode 424. Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1 

    string s = "AABBAB";
    int k = 2;
}

int main() {
    // Day 27 

    p1();


    return 0;
}