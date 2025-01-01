#include <iostream>
#include <unordered_map>

using namespace std;

string minWindow(string s, string t) {
    if (t.length() > s.length()) return "";

    // answer (start index, end index) 
    int x = 0, y = -1;

    // char map, which are in t 
    unordered_map<char, int> tCharFreq;
    int tChars = 0;

    // update char freq 
    for (char ch : t) {
        tCharFreq[ch]++;
        if (tCharFreq[ch] == 1) tChars++;
    }

    // find smallest answer window 
    for (int a = 0, b = 0; b < s.length(); b++) {
        // down the freq of t chars as we found one of them, 
        // or we have found a char which we dont need in our answer ans in future we can even remove it from the answer to reduce length 
        tCharFreq[s[b]]--;
        if (tCharFreq[s[b]] == 0) tChars--; // in case we find all freq of any char 

        // decrease the window size 
        while (tChars == 0) {
            // store the current answer, if its a valid one 
            if (y == -1 || (y - x + 1) > (b - a + 1)) y = b, x = a;

            // undo the L15, L16 work 
            tCharFreq[s[a]]++;
            if (tCharFreq[s[a]] == 1) tChars++;

            a++; // update left pointer 
        }
    }

    // return answer 
    if (y == -1) return "";
    return s.substr(x, y - x + 1);
}

string smallestWindow(string s, string t) {
    // Your code here
    if (t.length() > s.length()) return "-1";

    int x = 0, y = -1;

    int upperCase[26] = { 0 };
    int lowerCase[26] = { 0 };
    int tChars = 0;

    for (char ch : t) {
        if (ch >= 'A' && ch <= 'Z') {
            upperCase[ch - 'A']++;
            if (upperCase[ch - 'A'] == 1) tChars++;
        }
        if (ch >= 'a' && ch <= 'z') {
            upperCase[ch - 'a']++;
            if (upperCase[ch - 'a'] == 1) tChars++;
        }
    }

    for (int a = 0, b = 0; b < s.length(); b++) {
        if (s[b] >= 'A' && s[b] <= 'Z') {
            upperCase[s[b] - 'A']--;
            if (upperCase[s[b] - 'A'] == 0) tChars--;
        }
        if (s[b] >= 'a' && s[b] <= 'z') {
            upperCase[s[b] - 'a']--;
            if (upperCase[s[b] - 'a'] == 0) tChars--;
        }

        while (tChars == 0) {
            if (y == -1 || (y - x + 1) > (b - a + 1)) y = b, x = a;

            if (s[a] >= 'A' && s[a] <= 'Z') {
                upperCase[s[a] - 'A']++;
                if (upperCase[s[a] - 'A'] == 1) tChars++;
            }
            if (s[a] >= 'a' && s[a] <= 'z') {
                upperCase[s[a] - 'a']++;
                if (upperCase[s[a] - 'a'] == 1) tChars++;
            }

            a++;
        }
    }

    if (y == -1) return "-1";
    return s.substr(x, y - x + 1);

    // Complexity analysis : 
    // Time : O(|t| + (|s| + |s|))
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 76. Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1 

    string s = "practicecs";
    string t = "act";

    // string sub = minWindow(s, t);
    string sub = smallestWindow(s, t);
    cout << "sub :: " << sub << endl;
}

int main() {
    // Day 2 of June 

    p1();


    return 0;
}