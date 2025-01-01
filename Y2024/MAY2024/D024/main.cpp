#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int lengthOfLongestSubstring_Solution1(string s) {
    int longestSubstringLength = 0;

    for (int i = 0; i < s.length(); i++) {
        unordered_map<char, bool> characterOccurrence;
        int j = i;
        for (j; j < s.length(); j++) {
            if (characterOccurrence[s[j]]) break;
            characterOccurrence[s[j]] = true;
        }

        int len = j - i;
        if (longestSubstringLength < len) longestSubstringLength = len;
    }

    return longestSubstringLength;

    // Complexity 
    // Time : O(n * n) 
    // Space : O(n) 
}

int lengthOfLongestSubstring(string s) {
    int longestSubstringLength = 0;
    unordered_map<char, bool> characterOccurrence;

    int ptr1 = 0, ptr2 = 0;
    characterOccurrence[s[ptr1]] = true; // as we have taken s[ptr1] we will mark it true 
    while (ptr2 < s.length()) {
        int len = ptr2 - ptr1 + 1;
        if (longestSubstringLength < len) longestSubstringLength = len;
        // now if the next (or ptr2++) char is false in characterOccurrence
        // then do ptr2++ and mark it true in characterOccurrence 
        // otherwise do ptr1++ while ptr2++ does not becomes false 
        ptr2++;
        while (characterOccurrence[s[ptr2]]) characterOccurrence[s[ptr1++]] = false;

        characterOccurrence[s[ptr2]] = true;
    }

    return longestSubstringLength;

    // Complexity 
    // Time : O(n * n) 
    // Space : O(n) 
}

int longestUniqueSubsttr_Solution3(string s){
    // only if s only contains [a-z] 
    // code
    int longestSubstringLength = 0;
    int characterOccurrence[26] = { 0 };

    int ptr1 = 0, ptr2 = 0;
    characterOccurrence[s[ptr1] - 'a'] = 1;
    while (ptr2 < s.length()) {
        int len = ptr2 - ptr1 + 1;
        if (longestSubstringLength < len) longestSubstringLength = len;
        ptr2++;
        while (characterOccurrence[s[ptr2] - 'a']) {
            characterOccurrence[s[ptr1++] - 'a'] = 0;
        }

        characterOccurrence[s[ptr2] - 'a'] = 1;
    }

    return longestSubstringLength;
}

void p1() {
    // Problem 1 : Leetcode 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/ 
    // GeeksForGeeks https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1 

    // string str = "";
    string str = "adkjkffjkafdjklsakj;lfjfakkioruwkkjca sdsajdf;a";

    int len = lengthOfLongestSubstring(str);
    cout << "longest substr without repeating chars :: " << len << endl;
}

int main() {
    // Day 24 

    p1();


    return 0;
}