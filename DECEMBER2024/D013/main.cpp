#include <bits/stdc++.h>

using namespace std;


int getIndex(char c) {
    int index = 52;
    if (c >= 'a' && c <= 'z') index = c - 'a';
    if (c >= 'A' && c <= 'Z') index = c - 'A' + 26;

    return index;
}

char getChar(int index) {
    char ch = '$';
    if (index >= 0 && index <= 25) ch = 'a' + index;
    if (index >= 26 && index <= 51) ch = 'A' + index - 26;

    return ch;
}

vector<string> brute(vector<string>& words) {
    int N = words.size();
    vector<vector<int>> freqList(N, vector<int>(26, 0));

    for (int i = 0; i < N; i++) {
        for (char c : words[i]) {
            freqList[i][getIndex(c)]++;
        }
    }

    vector<string> out;

    for (int ci = 0; ci < 26; ci++) {
        int mini = INT_MAX;
        for (int i = 0; i < N; i++) mini = min(mini, freqList[i][ci]);
        string s(1, 'a' + ci);
        for (int i = 0; i < mini; i++) out.push_back(s);
    }

    return out;

    // Complexity analysis 
    // Time : O(N * max_str_len) + O(26 * (N + min_str_len)) 
    // Space : O(26 * N) 
}

vector<string> brute2(vector<string>& words) {
    int N = words.size();
    vector<int> minfreq(26, INT_MAX);

    for (int i = 0; i < N; i++) {
        vector<int> freq(26, 0);
        for (char c : words[i]) freq[getIndex(c)]++;
        for (int j = 0; j < 26; j++) minfreq[j] = min(minfreq[j], freq[j]);
    }

    vector<string> out;

    for (int ci = 0; ci < 26; ci++) {
        string s(1, 'a' + ci);
        for (int i = 0; i < minfreq[ci]; i++) out.push_back(s);
    }

    return out;

    // Complexity analysis 
    // Time : O(N * max_str_len) + O(26 * min_str_len) 
    // Space : O(26 * 2) 
}

vector<string> commonChars(vector<string>& words) {
    // brute force method 
    // return brute(words);

    // another brute 
    return brute2(words);
}

void p1() {
    // Problem 1 : Leetcode 1002. Find Common Characters - https://leetcode.com/problems/find-common-characters/ 

    vector<string> words = { "some", "done", "come" };
    vector<string> common = commonChars(words);
    for (string s : common) cout << s << " ";
    cout << endl;
}

string common_String(string s1, string s2) {
    // Code here
    vector<int> charFreqS1(52, 0);
    vector<int> charFreqS2(52, 0);

    for (char c : s1) charFreqS1[getIndex(c)]++;
    for (char c : s2) charFreqS2[getIndex(c)]++;

    string common = "";
    for (int i = 0; i < 52; i++) {
        int mini = min(charFreqS1[i], charFreqS2[i]);
        if (mini > 0) common += string(1, getChar(i));
    }

    sort(common.begin(), common.end());

    if (common.length() == 0) return "nil";
    return common;

    // Complexity analysis 
    // Time : O(s1_len) + O(s2_len) + O(52) + O(str_len * log(str_len)) 
    // Space : O(52 * 2) 
}

void p2() {
    // Problem 2 : Geeksforgeeks String of Commons - https://www.geeksforgeeks.org/problems/string-of-commons4503/0 

    cout << common_String("AzzauUU", "AzzauUU") << endl;
    cout << common_String("AzzauUUP", "AzzPauUU") << endl;
    cout << common_String("AzzauUUP", "AzzpauUU") << endl;
}


int main() {
    // Day 13 of December - Still understanding hashing 

    p1();

    p2();


    return 0;
}