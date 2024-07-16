#include <iostream>
#include <unordered_map>

using namespace std;

int lengthOfLongestSubstring(string s) {
    int n = s.length();

    int max_sub_len = 0; 
    unordered_map<char, int> freq;

    for (int l = 0, r = 0; r < n; r++) {
        freq[s[r]]++;

        while (freq[s[r]] > 1) freq[s[l++]]--;

        int sub_len = r - l + 1;
        max_sub_len = max(max_sub_len, sub_len);
    }

    return max_sub_len;
}

void p1() {
    // Problem 1 : Leetcode 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1 

    string s = "12s545s";
    int uniqueSubLen = lengthOfLongestSubstring(s);
    cout << "Longest Substring Without Repeating Characters ::" << uniqueSubLen << endl;
}

int main() {
    // Day 16 

    p1();


    return 0;
}