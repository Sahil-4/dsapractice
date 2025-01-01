#include <iostream>

using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;

    int freq1[26] = {0};
    int freq2[26] = {0};

    for (int i = 0; i < s.length(); i++) {
        int index1 = s[i] - 'a';
        int index2 = t[i] - 'a';

        freq1[index1]++;
        freq2[index2]++;
    }

    for (int i = 0; i < 26; i++) {
        if (freq1[i] != freq2[i]) return false;
    }

    return true;
}

void p1() {
    // Problem 1 : LC 242. Valid Anagram - https://leetcode.com/problems/valid-anagram/ 

    string s = "anagram", t = "nagaram";

    bool check = isAnagram(s, t);
    cout << "Check : " << check << endl;
}

void rotateOne(string &s) {
    char ch = s[0];
    for (int i = 0; i < s.length() - 1; i++) s[i] = s[i + 1];
    s[s.length() - 1] = ch;
}

bool rotateString(string s, string goal) {
    if (s.length() != goal.length()) return false;
    if (s == goal) return true;

    for (int i = 0; i < s.length(); i++) {
        rotateOne(s);
        if (s == goal) return true;
    }

    return false;
}

void p2() {
    // Problem 2 : LC 796. Rotate String - https://leetcode.com/problems/rotate-string/ 

    string s = "abcde", goal = "cdeab";

    bool possible = rotateString(s, goal);
    cout << "possible : " << possible << endl;
}

int main() {
    // Day 1 of April, overall Day 92 

    p1();

    p2();


    return 0;
}