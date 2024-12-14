#include <bits/stdc++.h>

using namespace std;

vector<vector<string>> sol1(vector<string>& strs) {
    map<string, vector<string>> mp;

    for (string s : strs) {
        string sc = string(s);
        sort(sc.begin(), sc.end());
        mp[sc].push_back(s);
    }

    vector<vector<string>> out;
    for (map<string, vector<string>>::iterator it = mp.begin(); it != mp.end(); it++) {
        out.push_back(it->second);
    }

    return out;

    // Complexity analysis 
    // Time : O(N * (K * log(K))) 
    // Space : O(N + Keys) for map 
}

string getHash(string s) {
    string hash = "";
    int freq[26] = { 0 };
    for (char c : s) freq[c - 'a']++;
    for (int f : freq) hash += to_string(f) + "$";
    return hash;
}

vector<vector<string>> sol2(vector<string>& strs) {
    map<string, vector<string>> mp;

    for (string s : strs) {
        string hash = getHash(s);
        mp[hash].push_back(s);
    }

    vector<vector<string>> out;
    for (auto it = mp.begin(); it != mp.end(); it++) {
        out.push_back(it->second);
    }

    // sorting - for gfg 
    // sort(out.begin(), out.end());

    return out;

    // Complexity analysis 
    // Time : O(N * K) 
    // Space : O(N + Keys) for map 
}

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // return sol1(strs);

    return sol2(strs);
}

void p1() {
    // Problem 1 : Leetcode 49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/print-anagrams-together/1 

    vector<string> strs = { "abc", "add", "daa", "cba", "bca", "aad", "dda" };
    vector<vector<string>> out = groupAnagrams(strs);

    for (vector<string> v : out) {
        for (string s : v) cout << s << " ";
        cout << endl;
    }
}


int main() {
    // Day 14 of December 

    p1();


    return 0;
}